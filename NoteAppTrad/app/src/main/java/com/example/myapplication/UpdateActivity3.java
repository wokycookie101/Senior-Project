package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class UpdateActivity3 extends AppCompatActivity {

    EditText updateTitle, updateDesc;
    Button updateBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_update3);
        updateBtn = findViewById(R.id.updateBtn);
        updateTitle = findViewById(R.id.updateTitle);
        updateDesc = findViewById(R.id.updateDesc);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);



        String title = getIntent().getStringExtra("title");
        String desc = getIntent().getStringExtra("description");
        int id = getIntent().getIntExtra("id", 0);
        updateTitle.setText(title);
        updateDesc.setText(desc);

        String sId = String.valueOf(id);


        updateBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                NoteHelper noteHelper = new NoteHelper(UpdateActivity3.this);
                noteHelper.updateData(updateTitle.getText().toString(), updateDesc.getText().toString(), sId);
                Toast.makeText(UpdateActivity3.this, "The Data is Successfully Added", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(UpdateActivity3.this, MainActivity.class));

            }
        });



    }
}