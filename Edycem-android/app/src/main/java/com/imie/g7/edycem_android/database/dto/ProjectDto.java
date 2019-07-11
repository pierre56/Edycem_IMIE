package com.imie.g7.edycem_android.database.dto;

public class ProjectDto {

    private int id;
    private String society;
    private String name;
    private int userId;

    public ProjectDto() {
    }

    public ProjectDto(int id, String society, String name, int userId) {
        this.id = id;
        this.society = society;
        this.name = name;
        this.userId = userId;
    }

    public ProjectDto(String society, String name, int userId) {
        this.society = society;
        this.name = name;
        this.userId = userId;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getSociety() {
        return society;
    }

    public void setSociety(String society) {
        this.society = society;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

}
