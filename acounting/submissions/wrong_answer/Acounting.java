package acounting.submissions.wrong_answer;

import java.util.ArrayList;
import java.util.Scanner;

public class Acounting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<Integer> a = new ArrayList<Integer>();

        for (int i = 1; i < n; i++) {
            a.add(sc.nextInt());
        }

        int sum = 0;

        for (Integer integer : a) {
            sum += integer;
        }

        System.out.println(sum);
    }
}
