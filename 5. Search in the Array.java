import java.util.*;
import java.io.*;

public class Solution {
    public static ArrayList<Integer> searchInTheArray(ArrayList<Integer> arr, ArrayList<Integer> queries, int n, int q) {

        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < q; i++) {
            int query = queries.get(i); // Get the current query element
            int sum = 0; // Initialize sum variable

            // Iterate through the arr array and add elements less than or equal to the query
            for (int j = 0; j < n; j++) {
                if (arr.get(j) <= query) {
                    sum += arr.get(j);
                }
            }

            // Add the calculated sum for the current query to the result array
            result.add(sum);
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine()); // Read the size of the array
        ArrayList<Integer> arr = new ArrayList<>(); // Initialize an empty array

        // Read the array elements
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(reader.readLine()));
        }

        int q = Integer.parseInt(reader.readLine()); // Read the size of the queries array
        ArrayList<Integer> queries = new ArrayList<>(); // Initialize an empty array

        // Read the query elements
        for (int i = 0; i < q; i++) {
            queries.add(Integer.parseInt(reader.readLine()));
        }

        ArrayList<Integer> result = searchInTheArray(arr, queries, n, q); // Call the searchInTheArray function

        // Print the result array
        for (int element : result) {
            System.out.println(element);
        }
    }
}
