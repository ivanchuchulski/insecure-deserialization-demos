package com.example.server;

import com.example.lib.Virus;

import java.io.IOException;
import java.io.InputStream;
import java.io.InvalidClassException;
import java.io.ObjectInputStream;
import java.io.ObjectStreamClass;
import java.time.LocalDate;
import java.util.List;

public class SafeVirusInputStream extends ObjectInputStream {
    private final List<String> supportedClasses =
            List.of(Virus.class.getName(), LocalDate.class.getName(), "java.time.Ser");

    public SafeVirusInputStream(InputStream in) throws IOException {
        super(in);
    }

    @Override
    protected Class<?> resolveClass(ObjectStreamClass input) throws IOException, ClassNotFoundException {
        if (!supportedClasses.contains(input.getName())) {
            throw new InvalidClassException("unsupported class", input.getName());
        }

        return super.resolveClass(input);
    }
}
