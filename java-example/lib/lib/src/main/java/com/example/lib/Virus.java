package com.example.lib;

import java.io.Serializable;
import java.time.LocalDate;

public class Virus implements Serializable {
    private static final long serialVersionID = 1234L;

    private String name;
    private String abbreviation;
    private LocalDate outbreakDate;

    public Virus(String name, String abbreviation, LocalDate outbreakDate) {
        this.name = name;
        this.abbreviation = abbreviation;
        this.outbreakDate = outbreakDate;
    }

    @Override
    public String toString() {
        return "Virus{" +
                "name='" + name + '\'' +
                ", abbreviation='" + abbreviation + '\'' +
                ", outbreakDate=" + outbreakDate +
                '}';
    }

    public void print() {
        System.out.println(toString());
    }
}
