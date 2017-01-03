public class Levenshtein {
 
    public static int distance(String a, String b) {
        a = a.toLowerCase();
        b = b.toLowerCase();
        // i == 0
        int [] costs = new int [b.length() + 1];
        for (int j = 0; j < costs.length; j++)
            costs[j] = j;
        for (int i = 1; i <= a.length(); i++) {
            // j == 0; nw = lev(i - 1, j)
            costs[0] = i;
            int nw = i - 1;
            for (int j = 1; j <= b.length(); j++) {
                int cj = Math.min(1 + Math.min(costs[j], costs[j - 1]), a.charAt(i - 1) == b.charAt(j - 1) ? nw : nw + 1);
                nw = costs[j];
                costs[j] = cj;
            }
        }
        return costs[b.length()];
    }
 
    public static void main(String [] args) {
        System.out.println("Comparing Cream to Cream Berkeley: " + distance("Cream", "Cream Berkeley"));
        System.out.println("Comparing Cream to CREAM Berkeley: " + distance("Cream", "CREAM Berkeley"));
        System.out.println("Comparing Artichoke Basille to Artichoke Basille's Pizza: " + distance("Artichoke Basille", "Artichoke Basille's Pizza"));
        System.out.println("Comparing Safeway to safeway Berkeley: " + distance("Safeway", "safeway"));
        System.out.println("Comparing TCgarden to T C Garden: " + distance("TCgarden", "T C Garden"));
        System.out.println("Comparing Cream to Safeway: " + distance("Cream", "Safeway"));
        // System.out.println("Comparing Cream to Cream Berkeley: " + distance("Cream", "Cream Berkeley"));

    }
}