import java.io.*;
import java.util.* ;

public class Solution {
    public static int[] ninjaAndSortedArrays(int arr1[], int arr2[], int m, int n) 
    {
        int arr3[]=new int[m+n];
        int k=0;
        for(int i=0; i<arr1.length; i++)
        {
            if(arr1[i]!=0)
                arr3[k++]=arr1[i];
        }
        for(int i=0; i<arr2.length; i++)
        {
            if(arr2[i]!=0)
                arr3[k++]=arr2[i];
        }
        Arrays.sort(arr3);
        return arr3;
    }
}
