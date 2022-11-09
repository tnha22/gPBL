/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Ve {

    private int id;
    private String ma;
    private Phim phim;
    private Khunggio khunggio;
    private Ghe ghe;

    public Ve() {
        super();
    }

    public Ve(int id, String ma, Phim phim, Khunggio khunggio, Ghe ghe) {
        this.id = id;
        this.ma = ma;
        this.phim = phim;
        this.khunggio = khunggio;
        this.ghe = ghe;
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

    public Phim getPhim() {
        return phim;
    }

    public void setPhim(Phim phim) {
        this.phim = phim;
    }

    public Khunggio getKhunggio() {
        return khunggio;
    }

    public void setKhunggio(Khunggio khunggio) {
        this.khunggio = khunggio;
    }

    public Ghe getGhe() {
        return ghe;
    }

    public void setGhe(Ghe ghe) {
        this.ghe = ghe;
    }
  
}