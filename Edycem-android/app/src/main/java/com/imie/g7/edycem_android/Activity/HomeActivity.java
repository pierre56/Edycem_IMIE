package com.imie.g7.edycem_android.activity;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import com.imie.g7.edycem_android.R;

public class HomeActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

    }

    public void clickButtonAddProject(View view) {
        Intent intent = new Intent(this, AddProjectActivity.class);
        //intent.putExtra("parametre", 123);
        startActivity(intent);
    }
}
