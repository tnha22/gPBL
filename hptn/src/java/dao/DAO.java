/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author ADMIN
 */
public class DAO {
    public static Connection con;
    
    public DAO(){
        if(con == null){
            String dbUrl = "jdbc:mysql://localhost:3306/hptn?autoReconnect=true&useSSL=false";
            String dbClass = "com.mysql.cj.jdbc.Driver";
            try {
                Class.forName(dbClass);
                con = DriverManager.getConnection (dbUrl, "root","12345678");
            }catch(ClassNotFoundException | SQLException e) {
                System.out.println(e);
            }
        }
        System.out.println(con);
    }
}