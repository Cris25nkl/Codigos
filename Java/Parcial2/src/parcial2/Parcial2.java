/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package parcial2;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import jdk.internal.org.objectweb.asm.Opcodes;

/**
 *
 * @author CRISTIAN DAVID FLOREZ LOPEZ-1974001
 */
public class Parcial2 extends JFrame implements ActionListener{

   JLabel e1,e2,e3,e4;
    JTextField c1,c2,c3,c4; 
    JButton b1,b2,b3,b4;
    JPanel p1,p2;
    Container contenedor;
    Manejador manejador;
    
    public Parcial2(){
       super("ventana");
       
       contenedor = getContentPane();
       contenedor.setLayout(new BorderLayout());
       
       e1 = new JLabel("Codigo");
       e2 = new JLabel("Nombre");
       e3 = new JLabel("Plan");
       e4 = new JLabel("Temperatura");
       
       c1 = new JTextField(12);
       c2 = new JTextField(12);
       c3 = new JTextField(12);
       c4 = new JTextField(12);
       
       b1 = new JButton("Guardar");
       b1.addActionListener(this);
      
       
       b2 = new JButton("Consultar");
       b2.addActionListener(this);
       
       p2 = new JPanel(new GridLayout(1,4));
       p2.add(b1);
       p2.add(b2);
     
       
       p1 = new JPanel(new GridLayout(4, 2));
       p1.add(e1);
       p1.add(c1);
       p1.add(e2);
       p1.add(c2);
       p1.add(e3);
       p1.add(c3);
       p1.add(e4);
       p1.add(c4);
       
       contenedor.add(p1,BorderLayout.CENTER);
       contenedor.add(p2, BorderLayout.SOUTH);
       manejador = new Manejador();
       
       setSize(400,200);
       setVisible(true);
   }
    
   
    public static void main(String[] args) {
        Parcial2 gui = new Parcial2();
        gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        
    }
    
    
    @Override
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource()== b1) {
            System.out.println("entra");
            manejador.CrearConexion();
                String codigo = c1.getText();
                String nombre = c2.getText();
                String plan = c3.getText();
                String temperatura = c4.getText();
                String estado ="";
 /*************************************************************************************************/
        //Lectura del archivo de texto
         File archivo = new File("temperatura.txt");
        String textoActual="";
        try {
            BufferedReader entrada = new BufferedReader(new FileReader(archivo));
            textoActual = entrada.readLine();
            System.out.println(textoActual);
            
        } catch (FileNotFoundException ex) {
            //Logger.getLogger(EjemploArchivos.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
           // Logger.getLogger(EjemploArchivos.class.getName()).log(Level.SEVERE, null, ex);
        }
        
            if (Integer.parseInt(textoActual)<37) {
                estado = "sano";
            }else{
                if (Integer.parseInt(textoActual)==37) {
                    estado= "bajo riesgo";
                }else estado="enfermo";
            }
             
 /*************************************************************************************************/
                
            
            String consulta = "INSERT INTO public.\"Estudiantes\"(\n" +
                                    "\"Codigo\", \"Nombre\", \"Plan\", \"Temperatura\", \"Estado\")\n" +
                                    "VALUES ('"+codigo+"', '"+nombre+"', '"+plan+"', '"+temperatura+"','"+estado+"');";
            
            manejador.insertarFilas(consulta);
            System.out.println("almenos entra");
            
        }else{
            if (ae.getSource()==b2) {
                manejador.consultarfilas();
            }
        }
    
}
}

