import 'package:flutter/material.dart';
import 'package:yourgarden/Screens/test.dart';
import 'package:yourgarden/Screens/word_cloud.dart';

import '../constants.dart';
import '../homepage.dart';

class MyBottomNavBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.only(
        left: kDefaultPadding * 2,
        right: kDefaultPadding * 2,
        bottom: kDefaultPadding / 4,
      ),
      height: 80,
      decoration: BoxDecoration(
        color: kButtonColor,
        boxShadow: [
          BoxShadow(
            offset: Offset(0, -10),
            blurRadius: 35,
            color: kPrimaryColor.withOpacity(0.38),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          IconButton(
            icon: Icon(Icons.chat),
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => MyChatScreen()));
            },
          ),
          IconButton(
            icon: Icon(Icons.grass),
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => BuyScreen()));
            },
          ),
          IconButton(
            icon: Icon(Icons.cloud),
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => WordCloud()));
            },
          ),
          IconButton(
            icon: Icon(Icons.assistant),
            onPressed: () {},
          ),
        ],
      ),
    );
  }
}