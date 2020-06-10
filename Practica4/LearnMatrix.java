import java.net.*;
import java.util.Stack;
import java.io.*;
import java.util.Scanner;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
public class LearnMatrix {

   public static ArrayList<ArrayList<Integer>> building(String name){
       System.out.print("HOLA");
        ArrayList<ArrayList<Integer>> Lista = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> Vector = new ArrayList<Integer>();
        File archivo = null;
        FileReader fr = null;
        BufferedReader br = null;
          try {
             archivo = new File (name);
             fr = new FileReader (archivo);
             br = new BufferedReader(fr);
             String linea=br.readLine();
             while(linea!=null){
                Vector.clear();
                String[] values = linea.split(",");
                
                for (int i = 0; i<values.length; i++) {
                    System.out.println(values[i]);
                    Vector.add(Integer.parseInt(Character.toString(values[i].charAt(0))));
                }
                Lista.add(Vector);
                linea=br.readLine();
            }
          }
          catch(Exception e){
             e.printStackTrace();
          }
          finally
          {
             try{                    
                if( null != fr ){   
                   fr.close();     
                }                  
             }catch (Exception e2){ 
                e2.printStackTrace();
             }
          }

          return Lista;
    }

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> Clase;
        ArrayList<ArrayList<Integer>> Patron;
        int [][] C;
        int N;
        int i,j;
        String archivoA;
        String archivoB;
        Scanner reader= new Scanner(System.in);
        Scanner readerA= new Scanner(System.in);
        Scanner readerB= new Scanner(System.in);

        System.out.println("Ingrese el nombre del archivo que contiene  A: ");
        archivoA=readerA.nextLine();
        System.out.println("Ingrese el nombre del archivo que contiene  B: ");
        archivoB=readerB.nextLine();
        Clase= building(archivoA);
        Patron=building(archivoB);
        

        System.out.println("Clases: ");
        for (i=0;i<Clase.size() ;i++ ) {
            for (j=0;j<Clase.get(i).size();j++ ) {
                System.out.print(Clase.get(i).get(j) + "\t");
            }
            System.out.println();
        }
        
        System.out.println("Patrones: ");
        for (i=0;i<Patron.size() ;i++ ) {
            for (j=0;j<Patron.get(i).size();j++ ) {
                System.out.print(Patron.get(i).get(j) + "\t");
            }
            System.out.println();
        }
        

       

    }
}