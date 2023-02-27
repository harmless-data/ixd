package com.example.consumptuition;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;


public class EndActivity extends AppCompatActivity {
    Button startShoppingBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_end);

        startShoppingBtn = findViewById(R.id.start_shopping_btn);
        startShoppingBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(EndActivity.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }

}