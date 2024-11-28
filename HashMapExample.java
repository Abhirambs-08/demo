import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        // Create a HashMap
        HashMap<String, Integer> map = new HashMap<>();

        // Adding key-value pairs to the HashMap
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Cherry", 3);
        map.put("Date", 4);

        // Display the HashMap
        System.out.println("HashMap: " + map);

        // Accessing values
        System.out.println("Value for key 'Banana': " + map.get("Banana"));

        // Checking if a key exists
        if (map.containsKey("Cherry")) {
            System.out.println("Cherry is present in the HashMap.");
        }

        // Removing a key-value pair
        map.remove("Date");
        System.out.println("After removing 'Date': " + map);

        // Iterating through the HashMap
        System.out.println("Iterating through the HashMap:");
        for (String key : map.keySet()) {
            System.out.println("Key: " + key + ", Value: " + map.get(key));
        }

        // Getting the size of the HashMap
        System.out.println("Size of the HashMap: " + map.size());

        // Clearing the HashMap
        map.clear();
        System.out.println("HashMap after clearing: " + map);
    }
}