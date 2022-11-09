/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Nguoidung {

    private int id;
    private Hoten hoten;
    private String tendangnhap;
    private String matkhau;
    private String ngaysinh;
    private Diachi diachi;
    private String email;
    private int String;
    private String ghichu;

    public Nguoidung() {
        super();
    }

    public Nguoidung(int id, Hoten hoten, String tendangnhap, String matkhau, String ngaysinh, Diachi diachi, String email, int String, String ghichu) {
        this.id = id;
        this.hoten = hoten;
        this.tendangnhap = tendangnhap;
        this.matkhau = matkhau;
        this.ngaysinh = ngaysinh;
        this.diachi = diachi;
        this.email = email;
        this.String = String;
        this.ghichu = ghichu;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Hoten getHoten() {
        return hoten;
    }

    public void setHoten(Hoten hoten) {
        this.hoten = hoten;
    }

    public String getTendangnhap() {
        return tendangnhap;
    }

    public void setTendangnhap(String tendangnhap) {
        this.tendangnhap = tendangnhap;
    }

    public String getMatkhau() {
        return matkhau;
    }

    public void setMatkhau(String matkhau) {
        this.matkhau = matkhau;
    }

    public String getNgaysinh() {
        return ngaysinh;
    }

    public void setNgaysinh(String ngaysinh) {
        this.ngaysinh = ngaysinh;
    }

    public Diachi getDiachi() {
        return diachi;
    }

    public void setDiachi(Diachi diachi) {
        this.diachi = diachi;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getString() {
        return String;
    }

    public void setString(int String) {
        this.String = String;
    }

    public String getGhichu() {
        return ghichu;
    }

    public void setGhichu(String ghichu) {
        this.ghichu = ghichu;
    }

}