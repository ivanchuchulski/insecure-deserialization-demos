package com.example.lib;

import java.io.Serial;
import java.io.Serializable;
import java.time.LocalDate;

public class Virus implements Serializable {
    @Serial
    private static final long serialVersionUID = 1234L;
    private final String name;
    private final String abbreviation;
    private final LocalDate outbreakDate;

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
        System.out.println(this);
    }
}
