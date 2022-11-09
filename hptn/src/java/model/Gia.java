/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Gia {

    private int id;
    private String ma;
    private float giave;

    public Gia() {
        super();
    }

    public Gia(int id, String ma, float giave) {
        this.id = id;
        this.ma = ma;
        this.giave = giave;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getMa() {
        return ma;
    }

    public void setMa(String ma) {
        this.ma = ma;
    }

    public float getGiave() {
        return giave;
    }

    public void setGiave(float giave) {
        this.giave = giave;
    }
       
}