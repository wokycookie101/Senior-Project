package com.example.noteappai;

import java.io.Serializable;

public class NoteModel implements Serializable {

    private int id;
    private String title;
    private String description;

    // Constructor for existing notes (with ID)
    public NoteModel(int id, String title, String description) {
        this.id = id;
        this.title = title;
        this.description = description;
    }

    // Constructor for new notes (no ID yet)
    public NoteModel(String title, String description) {
        this.title = title;
        this.description = description;
    }

    // Getters and setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    // Utility methods
    @Override
    public String toString() {
        return "NoteModel{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", description='" + description + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof NoteModel)) return false;
        NoteModel other = (NoteModel) obj;
        return id == other.id &&
                title.equals(other.title) &&
                description.equals(other.description);
    }

    @Override
    public int hashCode() {
        return id + title.hashCode() + description.hashCode();
    }
}