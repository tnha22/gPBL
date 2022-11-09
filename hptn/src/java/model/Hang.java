/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Hang {

    private int id;
    private String ten;
    private String gioithieu;
    private Diachi diachi;
    private Rapchieu[] listRapchieu;

    public Hang() {
        super();
    }

    public Hang(int id, String ten, String gioithieu, Diachi diachi, Rapchieu[] listRapchieu) {
        this.id = id;
        this.ten = ten;
        this.gioithieu = gioithieu;
        this.diachi = diachi;
        this.listRapchieu = listRapchieu;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTen() {
        return ten;
    }

    public void setTen(String ten) {
        this.ten = ten;
    }

    public String getGioithieu() {
        return gioithieu;
    }

    public void setGioithieu(String gioithieu) {
        this.gioithieu = gioithieu;
    }

    public Diachi getDiachi() {
        return diachi;
    }

    public void setDiachi(Diachi diachi) {
        this.diachi = diachi;
    }

    public Rapchieu[] getListRapchieu() {
        return listRapchieu;
    }

    public void setListRapchieu(Rapchieu[] listRapchieu) {
        this.listRapchieu = listRapchieu;
    }

}