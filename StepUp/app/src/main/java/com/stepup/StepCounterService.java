package com.stepup;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class StepCounterService extends Service {
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
