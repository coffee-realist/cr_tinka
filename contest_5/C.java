import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Random;
import java.util.Collections;

public class Main {
    public static boolean is_prime(int x) {
        for (int i = 2; i <= x / i; i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int prev_prime(int x) {
        while (true) {
            x--;
            if (is_prime(x)) {
                return x;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String a = scanner.next();
        String b = scanner.next();
        int p = 79;
        int n = Math.max(b.length() * 2, a.length());
        List<Long> pows1 = new ArrayList<>(1 + n);
        List<Long> pows2 = new ArrayList<>(1 + n);
        int minn = (int) 2e9;
        int maxx = (int) (2e9 + 1e8);
        int m_1 = prev_prime(minn + (new Random().nextInt(maxx - minn + 1)));
        int m_2 = prev_prime(minn + (new Random().nextInt(maxx - minn + 1)));
        pows1.add(1L % m_1);
        pows2.add(1L % m_2);
        for (int i = 1; i <= n; i++) {
            pows1.add((1L * pows1.get(i - 1) * p) % m_1);
            pows2.add((1L * pows2.get(i - 1) * p) % m_2);
        }
        List<Long> b_sum_1 = new ArrayList<>(b.length() * 2 + 1);
        List<Long> b_sum_2 = new ArrayList<>(b.length() * 2 + 1);
        b_sum_1.add(0L);
        b_sum_2.add(0L);
        for (int i = 1; i <= b.length() * 2; i++) {
            b_sum_1.add((b_sum_1.get(i - 1) + b.charAt(i % b.length()) * 1L * pows1.get(i - 1)) % m_1);
            b_sum_2.add((b_sum_2.get(i - 1) + b.charAt(i % b.length()) * 1L * pows2.get(i - 1)) % m_2);
        }
        List<Long> a_sum_1 = new ArrayList<>(a.length() + 1);
        List<Long> a_sum_2 = new ArrayList<>(a.length() + 1);
        a_sum_1.add(0L);
        a_sum_2.add(0L);
        for (int i = 1; i <= a.length(); i++) {
            a_sum_1.add((a_sum_1.get(i - 1) + a.charAt(i - 1) * 1L * pows1.get(i - 1)) % m_1);
            a_sum_2.add((a_sum_2.get(i - 1) + a.charAt(i - 1) * 1L * pows2.get(i - 1)) % m_2);
        }
        List<Pair<Long, Long>> occurrences = new ArrayList<>();
        for (int i = b.length(); i < b.length() * 2; i++) {
            long r_1 = ((b_sum_1.get(i) - b_sum_1.get(i - b.length()) + m_1) * pows1.get(n - i)) % m_1;
            long r_2 = ((b_sum_2.get(i) - b_sum_2.get(i - b.length()) + m_2) * pows2.get(n - i)) % m_2;
            Pair<Long, Long> cur = new Pair<>(r_1, r_2);
            occurrences.add(cur);
        }
        Collections.sort(occurrences);
        int result = 0;
        for (int i = b.length(); i <= a.length(); i++) {
            long r_1 = ((a_sum_1.get(i) - a_sum_1.get(i - b.length()) + m_1) * pows1.get(n - i)) % m_1;
            long r_2 = ((a_sum_2.get(i) - a_sum_2.get(i - b.length()) + m_2) * pows2.get(n - i)) % m_2;
            Pair<Long, Long> cur = new Pair<>(r_1, r_2);
            if (Collections.binarySearch(occurrences, cur) >= 0) {
                result++;
            }
        }
        System.out.println(result);
    }
}

class Pair<T1, T2> implements Comparable<Pair<T1, T2>> {
    public T1 first;
    public T2 second;

    public Pair(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public int compareTo(Pair<T1, T2> other) {
        int cmp1 = ((Comparable<T1>) first).compareTo(other.first);
        if (cmp1 != 0) {
            return cmp1;
        }
        return ((Comparable<T2>) second).compareTo(other.second);
    }
}

