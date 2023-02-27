package com.example.consumptuition;

import android.content.Intent;
import android.content.SharedPreferences;
import android.hardware.camera2.CameraCharacteristics;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import com.journeyapps.barcodescanner.ScanContract;
import com.journeyapps.barcodescanner.ScanOptions;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.MediaType;


import androidx.activity.result.ActivityResultLauncher;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class BarcodeScannerActivity extends AppCompatActivity {

    private static final int REQUEST_CODE_SCAN = 100;

    private Button scanButton, endShoppingButton;
    private List<String> scannedBarcodes = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_barcode_scanner);

        int SDK_INT = android.os.Build.VERSION.SDK_INT;
        if (SDK_INT > 8)
        {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                    .permitAll().build();
            StrictMode.setThreadPolicy(policy);

        }


        scanButton = findViewById(R.id.scan_button);
        scanButton.setOnClickListener(new View.OnClickListener() {

            // Register the launcher and result handler
            private final ActivityResultLauncher<ScanOptions> barcodeLauncher = registerForActivityResult(new ScanContract(),
                    result -> {
                        if(result.getContents() == null) {
                            Toast.makeText(BarcodeScannerActivity.this, "Cancelled", Toast.LENGTH_LONG).show();
                        } else {
                            Toast.makeText(BarcodeScannerActivity.this, "Scanned: " + result.getContents(), Toast.LENGTH_LONG).show();
                            scannedBarcodes.add(result.getContents());
                        }
                    });

            @Override
            public void onClick(View view) {
                barcodeLauncher.launch(new ScanOptions());
            }
        });

        endShoppingButton = findViewById(R.id.end_shopping_btn);
        endShoppingButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Send scanned barcodes to server
                OkHttpClient client = new OkHttpClient();
                MediaType mediaType = MediaType.parse("application/json");
                String requestJson = new Gson().toJson(scannedBarcodes);
                RequestBody body = RequestBody.create(mediaType, requestJson);
                Request request = new Request.Builder()
                        .url("http://192.168.0.101:3000/fetch/LIST/")
                        .post(body)
                        .build();
                try {
                    Response response = client.newCall(request).execute();
                    if (response.isSuccessful()) {
                        // Successful request
                        Toast.makeText(BarcodeScannerActivity.this, "Scanned barcodes sent to server", Toast.LENGTH_SHORT).show();
                    } else {
                        // Request failed
                        Toast.makeText(BarcodeScannerActivity.this, "Yeah", Toast.LENGTH_SHORT).show();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                    Toast.makeText(BarcodeScannerActivity.this, "Error sending scanned barcodes to server", Toast.LENGTH_SHORT).show();
                }
                // Start EndActivity
                Intent intent = new Intent(BarcodeScannerActivity.this, EndActivity.class);
                startActivity(intent);
            }
        });


    }

    @Override
    protected void onPause() {
        super.onPause();
        // Save scanned barcodes to shared preferences
        /*SharedPreferences sharedPreferences = getSharedPreferences("MyPrefs", MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putStringSet("scannedBarcodes", new HashSet<>(scannedBarcodes));
        editor.apply();*/
    }

    @Override
    protected void onResume() {
        super.onResume();
        /*SharedPreferences sharedPreferences = getSharedPreferences("MyPrefs", MODE_PRIVATE);
        scannedBarcodes = new ArrayList<>(sharedPreferences.getStringSet("scannedBarcodes", new HashSet<>()));*/
    }
}
