/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;
/**
 *
 * @author ADMIN
 */
public class Ghe {

    private int id;
    private String ten;
    private String loai;
    private Phongchieu phongchieu;
    private Gia gia;

    public Ghe() {
        super();
    }

    public Ghe(int id, String ten, String loai, Phongchieu phongchieu, Gia gia) {
        this.id = id;
        this.ten = ten;
        this.loai = loai;
        this.phongchieu = phongchieu;
        this.gia = gia;
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

    public String getLoai() {
        return loai;
    }

    public void setLoai(String loai) {
        this.loai = loai;
    }

    public Phongchieu getPhongchieu() {
        return phongchieu;
    }

    public void setPhongchieu(Phongchieu phongchieu) {
        this.phongchieu = phongchieu;
    }

    public Gia getGia() {
        return gia;
    }

    public void setGia(Gia gia) {
        this.gia = gia;
    }
       
}