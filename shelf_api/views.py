from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShelfLayout
from .serializers import ShelfLayoutSerializer

class ShelfIdentificationView(APIView):
    def post(self, request, format=None):
        serializer = ShelfLayoutSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            layout = serializer.validated_data['layout']
            input_data = eval(layout[0])

            print(layout)
            result =self.identify_result(input_data)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def identify_result(self, input_grid):
        shelf_identification_results = []
        # Define the shape and location for each letter
        product_list = ['G', 'M', 'N', 'B']
        for h in product_list:
            output = {}
            result_grid = []
            for row in input_grid:
                new_row = []
                for item in row:
                    if item == h:
                        new_row.append(1)
                    else:
                        new_row.append(0)
                result_grid.append(new_row)
            # print(result_grid)
            shape_location = self.identify_shapes(result_grid)
            for i, shape_info in enumerate(shape_location):
                # print(f"Type: {shape_info['Shape']}")
                # print(f"Location: {shape_info['Location']}")
                output[h] = {'shape': shape_info['Shape'], 'location': shape_info['Location']}
                shelf_identification_results.append(output)
        return shelf_identification_results

    def identify_shapes(self,result_grid):
        # Function to identify shapes of '1's in the input grid
        shapes = []  # List to store the identified shapes with positions

        # Helper function to determine if a cluster is a rectangle
        def is_rectangle(cluster):
            rows = len(cluster)
            cols = len(cluster[0])
            return all(sum(cluster[i]) == sum(cluster[0]) for i in range(rows)) and all(
                sum(cluster[i][j] for i in range(rows)) == rows for j in range(cols))

        # Helper function to classify a cluster
        def classify_shape(cluster):
            rows = len(cluster)
            cols = len(cluster[0])
            if rows == 1 and cols == 1:
                return "Point"
            elif rows == 1:
                return "Horizontal Line"
            elif cols == 1:
                return "Vertical Rectangle"
            elif is_rectangle(cluster):
                if rows == cols:
                    return "Square"
                elif rows > cols:
                    return "Vertical Rectangle"
                else:
                    return "Horizontal Rectangle"
            else:
                return "Polygon"

        # Iterate through the input grid
        for row in range(len(result_grid)):
            for col in range(len(result_grid[0])):
                if result_grid[row][col] == 1:
                    # Find the connected cluster of '1's
                    cluster = []
                    stack = [(row, col)]
                    while stack:
                        r, c = stack.pop()
                        if 0 <= r < len(result_grid) and 0 <= c < len(result_grid[0]) and result_grid[r][c] == 1:
                            cluster.append((r, c))
                            result_grid[r][c] = 0  # Mark as visited
                            stack.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

                    # Convert the cluster coordinates to a binary grid
                    min_row = min(row for row, _ in cluster)
                    max_row = max(row for row, _ in cluster)
                    min_col = min(col for _, col in cluster)
                    max_col = max(col for _, col in cluster)
                    cluster_grid = [[0] * (max_col - min_col + 1) for _ in range(max_row - min_row + 1)]
                    for r, c in cluster:
                        cluster_grid[r - min_row][c - min_col] = 1

                    # Classify the shape of the cluster
                    shape_type = classify_shape(cluster_grid)

                    # Calculate the position of the shape within the input grid
                    top_left = (min_row, min_col)
                    bottom_right = (max_row, max_col)
                    center = ((min_row + max_row) // 2, (min_col + max_col) // 2)

                    # Determine the location based on the position
                    if center[0] < len(result_grid) // 2:
                        location = "Top"
                    elif center[0] > len(result_grid) // 2:
                        location = "Bottom"
                    else:
                        location = ""

                    if center[1] < len(result_grid[0]) // 2:
                        location = " Left"
                    elif center[1] > len(result_grid[0]) // 2:
                        location = " Right"

                    # Store the shape information including its position and location
                    shape_info = {
                        "Shape": shape_type,
                        "Location": location.strip()  # Remove leading/trailing spaces
                    }

                    shapes.append(shape_info)

        return shapes