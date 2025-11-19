/**
 * Comprehensive demonstration of the Strategy Pattern in Java
 *
 * The Strategy pattern defines a family of algorithms, encapsulates each one,
 * and makes them interchangeable. Strategy lets the algorithm vary independently
 * from clients that use it.
 */

import java.util.ArrayList;
import java.util.List;

// Strategy interface
interface PaymentStrategy {
    void pay(double amount);
    String getName();
}

// Concrete Strategies
class CreditCardPayment implements PaymentStrategy {
    private String cardNumber;
    private String name;

    public CreditCardPayment(String cardNumber, String name) {
        this.cardNumber = cardNumber;
        this.name = name;
    }

    @Override
    public void pay(double amount) {
        System.out.println("  [CreditCard] Paid $" + String.format("%.2f", amount) +
                          " using card ending in " + cardNumber.substring(cardNumber.length() - 4));
    }

    @Override
    public String getName() { return "Credit Card"; }
}

class PayPalPayment implements PaymentStrategy {
    private String email;

    public PayPalPayment(String email) {
        this.email = email;
    }

    @Override
    public void pay(double amount) {
        System.out.println("  [PayPal] Paid $" + String.format("%.2f", amount) +
                          " from account: " + email);
    }

    @Override
    public String getName() { return "PayPal"; }
}

class CryptoPayment implements PaymentStrategy {
    private String walletAddress;

    public CryptoPayment(String walletAddress) {
        this.walletAddress = walletAddress;
    }

    @Override
    public void pay(double amount) {
        System.out.println("  [Crypto] Paid $" + String.format("%.2f", amount) +
                          " from wallet: " + walletAddress.substring(0, 8) + "...");
    }

    @Override
    public String getName() { return "Cryptocurrency"; }
}

// Context
class ShoppingCart {
    private List<Double> items = new ArrayList<>();
    private PaymentStrategy paymentStrategy;

    public void addItem(double price) {
        items.add(price);
    }

    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.paymentStrategy = strategy;
    }

    public double getTotal() {
        return items.stream().mapToDouble(Double::doubleValue).sum();
    }

    public void checkout() {
        double total = getTotal();
        if (paymentStrategy == null) {
            System.out.println("  Please select a payment method");
            return;
        }
        System.out.println("  Total: $" + String.format("%.2f", total));
        paymentStrategy.pay(total);
    }
}

// Sorting strategy example

interface SortStrategy {
    void sort(int[] array);
    String getName();
}

class BubbleSort implements SortStrategy {
    @Override
    public void sort(int[] array) {
        int n = array.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        System.out.println("  [BubbleSort] Array sorted using bubble sort");
    }

    @Override
    public String getName() { return "Bubble Sort"; }
}

class QuickSort implements SortStrategy {
    @Override
    public void sort(int[] array) {
        quickSort(array, 0, array.length - 1);
        System.out.println("  [QuickSort] Array sorted using quick sort");
    }

    private void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pi = partition(array, low, high);
            quickSort(array, low, pi - 1);
            quickSort(array, pi + 1, high);
        }
    }

    private int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (array[j] < pivot) {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;
        return i + 1;
    }

    @Override
    public String getName() { return "Quick Sort"; }
}

class MergeSort implements SortStrategy {
    @Override
    public void sort(int[] array) {
        mergeSort(array, 0, array.length - 1);
        System.out.println("  [MergeSort] Array sorted using merge sort");
    }

    private void mergeSort(int[] array, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(array, left, mid);
            mergeSort(array, mid + 1, right);
            merge(array, left, mid, right);
        }
    }

    private void merge(int[] array, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int i = left, j = mid + 1, k = 0;

        while (i <= mid && j <= right) {
            if (array[i] <= array[j]) {
                temp[k++] = array[i++];
            } else {
                temp[k++] = array[j++];
            }
        }

        while (i <= mid) temp[k++] = array[i++];
        while (j <= right) temp[k++] = array[j++];

        System.arraycopy(temp, 0, array, left, temp.length);
    }

    @Override
    public String getName() { return "Merge Sort"; }
}

class Sorter {
    private SortStrategy strategy;

    public void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    public void sort(int[] array) {
        if (strategy == null) {
            System.out.println("  Please set a sorting strategy");
            return;
        }
        strategy.sort(array);
    }
}

// Compression strategy example

interface CompressionStrategy {
    void compress(String filename);
}

class ZipCompression implements CompressionStrategy {
    @Override
    public void compress(String filename) {
        System.out.println("  [ZIP] Compressing " + filename + " to " + filename + ".zip");
    }
}

class GzipCompression implements CompressionStrategy {
    @Override
    public void compress(String filename) {
        System.out.println("  [GZIP] Compressing " + filename + " to " + filename + ".gz");
    }
}

class TarCompression implements CompressionStrategy {
    @Override
    public void compress(String filename) {
        System.out.println("  [TAR] Archiving " + filename + " to " + filename + ".tar");
    }
}

class FileCompressor {
    private CompressionStrategy strategy;

    public FileCompressor(CompressionStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(CompressionStrategy strategy) {
        this.strategy = strategy;
    }

    public void compress(String filename) {
        strategy.compress(filename);
    }
}

public class MainStrategy {
    public static void main(String[] args) {
        System.out.println("=== Strategy Pattern Demonstration ===\n");

        // Payment strategy example
        System.out.println("--- 1. Payment Strategy ---");

        ShoppingCart cart = new ShoppingCart();
        cart.addItem(29.99);
        cart.addItem(49.99);
        cart.addItem(19.99);

        System.out.println("\nPayment with Credit Card:");
        cart.setPaymentStrategy(new CreditCardPayment("1234567890123456", "John Doe"));
        cart.checkout();

        System.out.println("\nPayment with PayPal:");
        cart.setPaymentStrategy(new PayPalPayment("john.doe@email.com"));
        cart.checkout();

        System.out.println("\nPayment with Crypto:");
        cart.setPaymentStrategy(new CryptoPayment("0x742d35Cc6634C0532925a3b844Bc454e4438f44e"));
        cart.checkout();
        System.out.println();

        // Sorting strategy example
        System.out.println("--- 2. Sorting Strategy ---");

        Sorter sorter = new Sorter();
        int[] array1 = {64, 34, 25, 12, 22, 11, 90};
        int[] array2 = {64, 34, 25, 12, 22, 11, 90};
        int[] array3 = {64, 34, 25, 12, 22, 11, 90};

        System.out.println("\nOriginal array: [64, 34, 25, 12, 22, 11, 90]");

        sorter.setStrategy(new BubbleSort());
        sorter.sort(array1);

        sorter.setStrategy(new QuickSort());
        sorter.sort(array2);

        sorter.setStrategy(new MergeSort());
        sorter.sort(array3);

        System.out.print("\nSorted result: [");
        for (int i = 0; i < array1.length; i++) {
            System.out.print(array1[i]);
            if (i < array1.length - 1) System.out.print(", ");
        }
        System.out.println("]");
        System.out.println();

        // Compression strategy example
        System.out.println("--- 3. Compression Strategy ---");

        FileCompressor compressor = new FileCompressor(new ZipCompression());
        compressor.compress("document.pdf");

        compressor.setStrategy(new GzipCompression());
        compressor.compress("log.txt");

        compressor.setStrategy(new TarCompression());
        compressor.compress("project");

        System.out.println("\n=== Summary ===");
        System.out.println("Strategy pattern benefits:");
        System.out.println("  - Defines a family of algorithms");
        System.out.println("  - Encapsulates each algorithm");
        System.out.println("  - Makes algorithms interchangeable");
        System.out.println("  - Eliminates conditional statements");
        System.out.println("\nUse cases:");
        System.out.println("  - Multiple algorithms for same task");
        System.out.println("  - Algorithm selection at runtime");
        System.out.println("  - Isolating algorithm implementation details");
    }
}
