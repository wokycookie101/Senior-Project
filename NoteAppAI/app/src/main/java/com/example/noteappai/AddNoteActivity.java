package com.example.noteappai;

import android.content.Intent;
import android.os.Bundle;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class AddNoteActivity extends AppCompatActivity {

    // UI components
    private EditText edTitle, edDesc;
    private Button addButton;

    // Database helper
    private NoteHelper noteHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main2);

        // Initialize views
        edTitle = findViewById(R.id.edTitle);
        edDesc = findViewById(R.id.edDesc);
        addButton = findViewById(R.id.addButton);

        // Initialize database helper
        noteHelper = new NoteHelper(this);

        // Make activity fullscreen
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);

        // Handle button click
        addButton.setOnClickListener(view -> saveNote());
    }

    /**
     * Saves a new note to the database if inputs are valid.
     */
    private void saveNote() {
        String title = edTitle.getText().toString().trim();
        String desc = edDesc.getText().toString().trim();

        if (!title.isEmpty() && !desc.isEmpty()) {
            noteHelper.insertData(title, desc);

            Toast.makeText(this, "Note successfully added", Toast.LENGTH_SHORT).show();

            // Clear inputs
            edTitle.setText("");
            edDesc.setText("");

            // Return to main screen
            startActivity(new Intent(this, MainActivity.class));
            finish(); // ✅ Prevents stacking multiple activities
        } else {
            Toast.makeText(this, "Title or description cannot be empty", Toast.LENGTH_SHORT).show();
        }
    }
}