import 'package:flutter/material.dart';
import 'package:yourgarden/Screens/Login_Screen.dart';
import 'package:yourgarden/constants.dart';

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        // textBaseline: TextBaseline.alphabetic,
        children: [
          Padding(
            padding: EdgeInsets.only(top: 100),
            child: Center(
              child: Text(
                "Welcome to YourGarden",
                style: TextStyle(fontSize: 30, color: kButtonColor),
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(left: 20, top: 50),
            child: Align(
              alignment: Alignment.centerLeft,
              child: Text(
                "Your One stop for everything in your garden",
                style: TextStyle(fontSize: 20),
                textAlign: TextAlign.left,
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(left: 20, top: 20),
            child: Align(
              alignment: Alignment.centerLeft,
              child: Text(
                "We have an in house chat bot to help with all your garden or plant realted questions. It is trained to understand questions like tell me more about sunflower or what plant goes well with basil? or What should I plant if its summer out here? You can also see all your searhces in a word cloud and it also comes with a companion app where you can create your own garden in your own backyard in AR!",
                style: TextStyle(fontSize: 10, color: kButtonColor),
                textAlign: TextAlign.left,
              ),
            ),
          ),
          SizedBox(
            height: 30,
          ),
          Spacer(),
          Align(
            alignment: Alignment.bottomRight,
            child: ElevatedButton(
              // color: Colors.white60,
              child: Text(
                "Enter",
                style: TextStyle(fontSize: 20),
              ),
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => LoginPage()));
              },
            ),
          )
        ],
      ),
    );
  }
}
