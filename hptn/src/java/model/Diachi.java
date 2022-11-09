/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package model;

/**
 *
 * @author ADMIN
 */
public class Diachi {

    private int id;
    private String sonha;
    private String toanha;
    private String duong;
    private String phuongxa;
    private String quanhuyen;
    private String thanhpho;

    public Diachi() {
        super();
    }
        
    public Diachi(int id, String sonha, String toanha, String duong, String phuongxa, String quanhuyen, String thanhpho) {
        this.id = id;
        this.sonha = sonha;
        this.toanha = toanha;
        this.duong = duong;
        this.phuongxa = phuongxa;
        this.quanhuyen = quanhuyen;
        this.thanhpho = thanhpho;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getSonha() {
        return sonha;
    }

    public void setSonha(String sonha) {
        this.sonha = sonha;
    }

    public String getToanha() {
        return toanha;
    }

    public void setToanha(String toanha) {
        this.toanha = toanha;
    }

    public String getDuong() {
        return duong;
    }

    public void setDuong(String duong) {
        this.duong = duong;
    }

    public String getPhuongxa() {
        return phuongxa;
    }

    public void setPhuongxa(String phuongxa) {
        this.phuongxa = phuongxa;
    }

    public String getQuanhuyen() {
        return quanhuyen;
    }

    public void setQuanhuyen(String quanhuyen) {
        this.quanhuyen = quanhuyen;
    }

    public String getThanhpho() {
        return thanhpho;
    }

    public void setThanhpho(String thanhpho) {
        this.thanhpho = thanhpho;
    }
    
}