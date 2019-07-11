package com.imie.g7.edycem_android.database.webservice;

import android.util.Log;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.json.JSONObject;

import cz.msebera.android.httpclient.Header;

public class UsersService {

    private static final String BASE_URL = "/edycem/";

    private static AsyncHttpClient client = new AsyncHttpClient();

    public static void get(String email) {
        client.get(getAbsoluteUrl(email), new AsyncHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers,
                                  byte[] responseBody) {
                String response = new String(responseBody);
                Log.println(1,"response : ", response);
                try {
                    JSONObject jsonObject = new JSONObject(response);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, byte[] responseBody,
                                  Throwable error) {
                Log.getStackTraceString(error);
            }
        });
    }


    private static String getAbsoluteUrl(String relativeUrl) {
        return BASE_URL + relativeUrl;
    }

}
