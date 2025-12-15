package com.example.noteappai;

import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class NoteAdapter extends RecyclerView.Adapter<NoteAdapter.ViewHolder> {

    private final Context context;
    private final List<NoteModel> noteList;

    public NoteAdapter(Context context, List<NoteModel> noteList) {
        this.context = context;
        this.noteList = noteList;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.note_item, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        NoteModel note = noteList.get(position);

        holder.tvTitle.setText(note.getTitle());
        holder.tvDesc.setText(note.getDescription());

        // Handle delete on long press
        holder.cardView.setOnLongClickListener(view -> {
            new AlertDialog.Builder(context)
                    .setTitle("Delete Entry")
                    .setMessage("Are you sure you want to delete this entry?")
                    .setPositiveButton("OK", (dialog, which) -> {
                        NoteHelper noteHelper = new NoteHelper(context);
                        noteHelper.deleteData(String.valueOf(note.getId()));

                        // Update list locally instead of restarting activity
                        noteList.remove(position);
                        notifyItemRemoved(position);

                        dialog.dismiss();
                    })
                    .setNegativeButton("CANCEL", (dialog, which) -> dialog.dismiss())
                    .setIcon(R.drawable.baseline_add_alert_24)
                    .show();
            return true;
        });

        // Handle click → open update screen
        holder.cardView.setOnClickListener(view -> {
            Intent intent = new Intent(context, UpdateNoteActivity.class);
            intent.putExtra("title", note.getTitle());
            intent.putExtra("description", note.getDescription());
            intent.putExtra("id", note.getId());
            context.startActivity(intent);
        });
    }

    @Override
    public int getItemCount() {
        return noteList.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvTitle, tvDesc;
        CardView cardView;

        ViewHolder(@NonNull View itemView) {
            super(itemView);
            tvTitle = itemView.findViewById(R.id.tvTitle);
            tvDesc = itemView.findViewById(R.id.tvDesc);
            cardView = itemView.findViewById(R.id.cardView);
        }
    }
}