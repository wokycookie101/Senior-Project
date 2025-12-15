package com.example.noteappai;

import android.content.Intent;
import android.database.Cursor;
import android.os.Bundle;
import android.view.WindowManager;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    // UI components
    private FloatingActionButton floatingId;
    private RecyclerView recyclerView;

    // Data + helper classes
    private ArrayList<NoteModel> noteList = new ArrayList<>();
    private NoteHelper noteHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Enable edge-to-edge layout (modern Android styling)
        EdgeToEdge.enable(this);

        // Set the layout for this activity
        setContentView(R.layout.activity_main);

        // Initialize views
        floatingId = findViewById(R.id.floatingId);
        recyclerView = findViewById(R.id.recyclerView);

        // Initialize database helper
        noteHelper = new NoteHelper(this);

        // Make the activity fullscreen
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);

        // Setup RecyclerView with a vertical list layout
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Load notes from database
        loadNotes();

        // Handle FAB click → open MainActivity2
        floatingId.setOnClickListener(view ->
                startActivity(new Intent(MainActivity.this, AddNoteActivity.class))
        );
    }

    /**
     * Loads notes from the database into the RecyclerView.
     */
    private void loadNotes() {
        Cursor cursor = noteHelper.showData();

        // Clear list before reloading (avoids duplicates if called again)
        noteList.clear();

        while (cursor.moveToNext()) {
            noteList.add(new NoteModel(
                    cursor.getInt(0),     // id
                    cursor.getString(1),  // title
                    cursor.getString(2)   // content
            ));
        }

        cursor.close(); // ✅ Always close cursor to avoid memory leaks

        // Attach adapter
        NoteAdapter adapter = new NoteAdapter(this, noteList);
        recyclerView.setAdapter(adapter);
    }
}