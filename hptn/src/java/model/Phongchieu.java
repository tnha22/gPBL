/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Phongchieu {

    private int id;
    private String ma;
    private String ten;
    private String soluongghe;
    private String dacdiem;
    private String trangthai;
    private Rapchieu rapchieu;
    private Ghe[] listGhe;

    public Phongchieu() {
        super();
    }

    public Phongchieu(int id, String ma, String ten, String soluongghe, String dacdiem, String trangthai, Rapchieu rapchieu, Ghe[] listGhe) {
        this.id = id;
        this.ma = ma;
        this.ten = ten;
        this.soluongghe = soluongghe;
        this.dacdiem = dacdiem;
        this.trangthai = trangthai;
        this.rapchieu = rapchieu;
        this.listGhe = listGhe;
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

    public String getTen() {
        return ten;
    }

    public void setTen(String ten) {
        this.ten = ten;
    }

    public String getSoluongghe() {
        return soluongghe;
    }

    public void setSoluongghe(String soluongghe) {
        this.soluongghe = soluongghe;
    }

    public String getDacdiem() {
        return dacdiem;
    }

    public void setDacdiem(String dacdiem) {
        this.dacdiem = dacdiem;
    }

    public String getTrangthai() {
        return trangthai;
    }

    public void setTrangthai(String trangthai) {
        this.trangthai = trangthai;
    }

    public Rapchieu getRapchieu() {
        return rapchieu;
    }

    public void setRapchieu(Rapchieu rapchieu) {
        this.rapchieu = rapchieu;
    }

    public Ghe[] getListGhe() {
        return listGhe;
    }

    public void setListGhe(Ghe[] listGhe) {
        this.listGhe = listGhe;
    }
    
}