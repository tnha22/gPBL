/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Rapchieu {

    private int id;
    private String ten;
    private String gioithieu;
    private Diachi diachi;
    private Phongchieu[] listPhongchieu;
    private String marap;

    public Rapchieu() {
        super();
    }

    public Rapchieu(int id, String ten, String gioithieu, Diachi diachi, Phongchieu[] listPhongchieu, String marap) {
        this.id = id;
        this.ten = ten;
        this.gioithieu = gioithieu;
        this.diachi = diachi;
        this.listPhongchieu = listPhongchieu;
        this.marap = marap;
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

    public Phongchieu[] getListPhongchieu() {
        return listPhongchieu;
    }

    public void setListPhongchieu(Phongchieu[] listPhongchieu) {
        this.listPhongchieu = listPhongchieu;
    }

    public String getMarap() {
        return marap;
    }

    public void setMarap(String marap) {
        this.marap = marap;
    }
 
}