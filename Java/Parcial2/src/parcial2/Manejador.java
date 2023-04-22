/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package parcial2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author CRISTIAN
 */
public final class Manejador {
    Connection conexion;
    JTable tabla;
    JScrollPane scroll;
    DefaultTableModel modelo;
    
    public Manejador(){
        CrearConexion();
    }
    public void CrearConexion(){
        System.out.println("hace conexion");
       conexion = null;
        
        try {
             conexion = DriverManager.getConnection
                    ("jdbc:postgresql://localhost:5432/postgres",//ruta local donde esta la base de datos
                     "postgres", //usuario
                     "cristianflorez25");//contraseña
        } catch (SQLException ex) {
            System.out.println("Algo salio mal con la conexion");
        }
    }
 
   
    
    /***********************************************************************************************/
    //Crear la conexion con laa base de datos
   public void CerrarConexion(){
        try {
            conexion.close();
        } catch (SQLException e) {
            System.out.println("No se pudo cerrar el archivo");
        }
    }
   /****************************************************************************************/
    //Insertar los datos en las columnas
   public void insertarFilas(String consulta){
        CrearConexion();
        
        try {
            Statement s = conexion.createStatement();
            s.executeLargeUpdate(consulta);
        } catch (SQLException ex) {
            System.out.println("Hubo error en la consulta");       
        }
        CerrarConexion();
    }
    /************************************************************************************************/
    //Creacion de la consulta
    public void crearmodelo(){
        modelo = new DefaultTableModel();
        modelo.addColumn("Codigo");
        modelo.addColumn("Nombre");
        modelo.addColumn("Plan");
        modelo.addColumn("Temperatura");
        modelo.addColumn("Estado");
        tabla = new JTable(modelo);
        scroll = new JScrollPane(tabla);
        
        
    }
    public void consultarfilas(){
        CrearConexion();
        crearmodelo();
        
        try {
            System.out.println("entra aqui");
            Statement s = conexion.createStatement();
            String consulta = "SELECT \"Codigo\", \"Nombre\", \"Plan\", \"Temperatura\", \"Estado\"\n" +
                              "FROM public.\"Estudiantes\";";
            ResultSet resultado = s.executeQuery(consulta);
            
            while (resultado.next()) {
                Object arreglo[]= new Object[5];
                  for (int i = 0; i < 5; i++) {
                    arreglo[i] = resultado.getObject(i+1);
                    
                }
                  modelo.addRow(arreglo);
            }
            
        } catch (Exception e) {
            System.out.println("algo salio mal");
        }
        
        
        CerrarConexion();
        JOptionPane.showMessageDialog(tabla, scroll);
    }
    
            
}
