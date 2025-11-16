class Solution {
    public double average(int[] salary) {
        int min = salary[0];
        int max = salary[0];
        int sum = salary[0];

        for(int i = 1; i <= salary.length-1; i++) {
            if(salary[i] > max) {
                max = salary[i];
            }
            else if(salary[i] < min) {
                min = salary[i];
            }
            sum += salary[i];
        }
        double avgSalary = (double)(sum - min - max)/(salary.length-2);
        return avgSalary;
    }
}