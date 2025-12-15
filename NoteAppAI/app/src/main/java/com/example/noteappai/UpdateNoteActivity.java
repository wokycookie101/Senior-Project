package com.example.noteappai;

import android.content.Intent;
import android.os.Bundle;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class UpdateNoteActivity extends AppCompatActivity {

    private EditText updateTitle, updateDesc;
    private Button updateBtn;
    private NoteHelper noteHelper;

    private int noteId; // store ID directly

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_update3);

        // Initialize views
        updateBtn = findViewById(R.id.updateBtn);
        updateTitle = findViewById(R.id.updateTitle);
        updateDesc = findViewById(R.id.updateDesc);

        // Initialize database helper
        noteHelper = new NoteHelper(this);

        // Fullscreen mode
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);

        // Get data from intent
        String title = getIntent().getStringExtra("title");
        String desc = getIntent().getStringExtra("description");
        noteId = getIntent().getIntExtra("id", 0);

        // Pre-fill fields
        updateTitle.setText(title);
        updateDesc.setText(desc);

        // Handle update button click
        updateBtn.setOnClickListener(v -> updateNote());
    }

    /**
     * Updates the note in the database.
     */
    private void updateNote() {
        String newTitle = updateTitle.getText().toString().trim();
        String newDesc = updateDesc.getText().toString().trim();

        if (!newTitle.isEmpty() && !newDesc.isEmpty()) {
            noteHelper.updateData(newTitle, newDesc, String.valueOf(noteId));
            Toast.makeText(this, "Note updated successfully", Toast.LENGTH_SHORT).show();

            // Return to main screen without stacking activities
            startActivity(new Intent(this, MainActivity.class));
            finish();
        } else {
            Toast.makeText(this, "Title or description cannot be empty", Toast.LENGTH_SHORT).show();
        }
    }
}