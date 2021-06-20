import 'package:flutter/material.dart';
import 'package:yourgarden/Screens/splash_screen.dart';
import 'package:yourgarden/constants.dart';
import 'package:dotted_border/dotted_border.dart';

import 'Screens/Login_Screen.dart';
import 'components/form_field.dart';
import 'components/my_button.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData.dark().copyWith(
        primaryColor: kPrimaryColor,
        scaffoldBackgroundColor: kPrimaryColor,
        accentColor: kPrimaryColor,
        buttonColor: kButtonColor,
        textTheme: TextTheme(
          headline6: TextStyle(
            color: kButtonColor,
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ButtonStyle(
            backgroundColor: MaterialStateProperty.all<Color>(kButtonColor),
          ),
        ),
      ),
      home: SplashScreen(),
    );
  }
}
