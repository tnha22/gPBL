/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

import java.util.Date;

/**
 *
 * @author ADMIN
 */
public class Lichchieu {

    private int id;
    private String ma;
    private Date ngaythang;
    private Phim phim;
    private String trangthai;
    private Khunggio khunggio;
    private Phongchieu phongchieu;
    private Quanli quanli;

    public Lichchieu() {
    }

    public Lichchieu(int id, String ma, Date ngaythang, Phim phim, String trangthai, Khunggio khunggio, Phongchieu phongchieu, Quanli quanli) {
        this.id = id;
        this.ma = ma;
        this.ngaythang = ngaythang;
        this.phim = phim;
        this.trangthai = trangthai;
        this.khunggio = khunggio;
        this.phongchieu = phongchieu;
        this.quanli = quanli;
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

    public Date getNgaythang() {
        return ngaythang;
    }

    public void setNgaythang(Date ngaythang) {
        this.ngaythang = ngaythang;
    }

    public Phim getPhim() {
        return phim;
    }

    public void setPhim(Phim phim) {
        this.phim = phim;
    }

    public String getTrangthai() {
        return trangthai;
    }

    public void setTrangthai(String trangthai) {
        this.trangthai = trangthai;
    }

    public Khunggio getKhunggio() {
        return khunggio;
    }

    public void setKhunggio(Khunggio khunggio) {
        this.khunggio = khunggio;
    }

    public Phongchieu getPhongchieu() {
        return phongchieu;
    }

    public void setPhongchieu(Phongchieu phongchieu) {
        this.phongchieu = phongchieu;
    }

    public Quanli getQuanli() {
        return quanli;
    }

    public void setQuanli(Quanli quanli) {
        this.quanli = quanli;
    }

}