// Flutter web plugin registrant file.
//
// Generated file. Do not edit.
//

// @dart = 2.13
// ignore_for_file: type=lint

import 'package:audio_session/audio_session_web.dart';
import 'package:image_picker_for_web/image_picker_for_web.dart';
import 'package:just_audio_web/just_audio_web.dart';
import 'package:kakao_flutter_sdk_common/src/web/kakao_flutter_sdk_plugin.dart';
import 'package:permission_handler_html/permission_handler_html.dart';
import 'package:record_web/record_web.dart';
import 'package:shared_preferences_web/shared_preferences_web.dart';
import 'package:flutter_web_plugins/flutter_web_plugins.dart';

void registerPlugins([final Registrar? pluginRegistrar]) {
  final Registrar registrar = pluginRegistrar ?? webPluginRegistrar;
  AudioSessionWeb.registerWith(registrar);
  ImagePickerPlugin.registerWith(registrar);
  JustAudioPlugin.registerWith(registrar);
  KakaoFlutterSdkPlugin.registerWith(registrar);
  WebPermissionHandler.registerWith(registrar);
  RecordPluginWeb.registerWith(registrar);
  SharedPreferencesPlugin.registerWith(registrar);
  registrar.registerMessageHandler();
}
