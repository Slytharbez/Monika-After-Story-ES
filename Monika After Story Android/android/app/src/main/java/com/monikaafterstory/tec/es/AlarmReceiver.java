package com.monikaafterstory.tec.es;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.os.Build;
import androidx.core.app.NotificationCompat;
import android.graphics.Color;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

public class AlarmReceiver extends BroadcastReceiver {

    private static final String CHANNEL_ID = "mas_notifications_channel";
    private static final String CHANNEL_NAME = "Monika After Story";
    private static final String CHANNEL_DESC = "Notificaciones de Monika";

    @Override
    public void onReceive(Context context, Intent intent) {

        // 1. Extract Data from Intent
        String title = intent.getStringExtra("title");
        String message = intent.getStringExtra("message");
        int notifId = intent.getIntExtra("id", 1001);

        if (title == null)
            title = "Monika After Story";
        if (message == null)
            message = "Monika te está esperando.";

        NotificationManager notificationManager = (NotificationManager) context
                .getSystemService(Context.NOTIFICATION_SERVICE);

        // 2. Create Notification Channel (Required for Android 8.0+ / API 26+)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel channel = new NotificationChannel(
                    CHANNEL_ID,
                    CHANNEL_NAME,
                    NotificationManager.IMPORTANCE_HIGH);
            channel.setDescription(CHANNEL_DESC);
            channel.enableLights(true);
            channel.setLightColor(Color.rgb(255, 105, 180)); // Monika Pink
            channel.enableVibration(true);

            // Register the channel with the system
            notificationManager.createNotificationChannel(channel);
        }

        // 3. Create Launch Intent (Open Game on Click)
        // Uses getLaunchIntentForPackage to ensure we find the correct MainActivity
        Intent launchIntent = context.getPackageManager().getLaunchIntentForPackage(context.getPackageName());

        int flags = PendingIntent.FLAG_UPDATE_CURRENT;
        if (Build.VERSION.SDK_INT >= 31) { // Android 12+ requires MUTABLE/IMMUTABLE flag
            flags |= PendingIntent.FLAG_IMMUTABLE;
        }

        PendingIntent pendingIntent = null;
        if (launchIntent != null) {
            pendingIntent = PendingIntent.getActivity(context, 0, launchIntent, flags);
        }

        // 4. Resolve Icons
        // Small Icon: 'ic_stat_smoll'
        int smallIconId = context.getResources().getIdentifier("ic_stat_smoll", "drawable", context.getPackageName());
        if (smallIconId == 0) {
            // Fallback to system default if custom icon missing
            smallIconId = android.R.drawable.sym_def_app_icon;
        }

        // Large Icon: 'ic_stat_large'
        Bitmap largeIconBitmap = null;
        int largeIconId = context.getResources().getIdentifier("ic_stat_large", "drawable", context.getPackageName());

        if (largeIconId != 0) {
            try {
                largeIconBitmap = BitmapFactory.decodeResource(context.getResources(), largeIconId);
            } catch (Exception e) {
                // If decode fails, ignore
            }
        }

        // Fallback for Large Icon: 'ic_launcher' (mipmap)
        if (largeIconBitmap == null) {
            int launcherIconId = context.getResources().getIdentifier("ic_launcher", "mipmap",
                    context.getPackageName());
            if (launcherIconId != 0) {
                try {
                    largeIconBitmap = BitmapFactory.decodeResource(context.getResources(), launcherIconId);
                } catch (Exception e) {
                }
            }
        }

        // 5. Build Notification
        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, CHANNEL_ID)
                .setSmallIcon(smallIconId)
                .setContentTitle(title)
                .setContentText(message)
                .setPriority(NotificationCompat.PRIORITY_HIGH)
                .setAutoCancel(true)
                .setVibrate(new long[] { 0, 500, 200, 500 }); // Vibration pattern

        if (largeIconBitmap != null) {
            builder.setLargeIcon(largeIconBitmap);
        }

        if (pendingIntent != null) {
            builder.setContentIntent(pendingIntent);
        }

        // 6. Show Notification
        notificationManager.notify(notifId, builder.build());
    }
}
