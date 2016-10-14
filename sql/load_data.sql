INSERT INTO User VALUES ('sportslover', 'Paul', 'Walker', 'sha512$8ec61415f1eb4afba45fa95e164a73e5$a8156f5e122a936e55512ccad145e72581c20853d8ceee8fc4ab535bead173dfb6625dd1d0eaccc9ace73008c135ef5eecb0b452470d007fde088602659ad9a2', 'sportslover@hotmail.com');

INSERT INTO Album (title,username,access)
  VALUES ('I love sports','sportslover','public');

INSERT INTO Photo(picid,format)
VALUES('b94f256c23dec8a2c0da546849058d9e','jpg');

INSERT INTO Photo(picid,format)
VALUES('01e37cbdd55913df563f527860b364e8','jpg');

INSERT INTO Photo(picid,format)
VALUES('8d554cd1d8bb7b49ca798381d1fc171b','jpg');

INSERT INTO Photo(picid,format)
VALUES('2e9e69e19342b98141789925e5f87f60','jpg');

INSERT INTO Photo(picid,format)
VALUES('298e8943ef1942159ef88be21c4619c9','jpg');

INSERT INTO Photo(picid,format)
VALUES('cefe45eaeaeb599256dda325c2e972da','jpg');

INSERT INTO Photo(picid,format)
VALUES('bf755d13bb78e1deb59ef66b6d5c6a70','jpg');

INSERT INTO Photo(picid,format)
VALUES('5f8d7957874f1303d8300e50f17e46d6','jpg');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(0, LAST_INSERT_ID(),'b94f256c23dec8a2c0da546849058d9e','sports pic 1');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(1, LAST_INSERT_ID(),'01e37cbdd55913df563f527860b364e8','sports pic 2');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(2, LAST_INSERT_ID(),'8d554cd1d8bb7b49ca798381d1fc171b','sports pic 3');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(3, LAST_INSERT_ID(),'2e9e69e19342b98141789925e5f87f60','sports pic 4');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(4, LAST_INSERT_ID(),'298e8943ef1942159ef88be21c4619c9','sports pic 5');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(5, LAST_INSERT_ID(),'cefe45eaeaeb599256dda325c2e972da','sports pic 6');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(6, LAST_INSERT_ID(),'bf755d13bb78e1deb59ef66b6d5c6a70','sports pic 7');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(7, LAST_INSERT_ID(),'5f8d7957874f1303d8300e50f17e46d6','sports pic 8');

INSERT INTO Album(title,username,access)
VALUES('I love football','sportslover','private');

INSERT INTO Photo(picid,format)
VALUES('001025dd643b0eb0661e359de86e3ea9','jpg');

INSERT INTO Photo(picid,format)
VALUES('9a0a7d25af4f7a73f67dde74e8e54cff','jpg');

INSERT INTO Photo(picid,format)
VALUES('c8e60100f13ffe374d59e39dc4b6a318','jpg');

INSERT INTO Photo(picid,format)
VALUES('5e8b6207f007338243d3e29d6b82acab','jpg');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(8, LAST_INSERT_ID(),'001025dd643b0eb0661e359de86e3ea9','football pic 1');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(9, LAST_INSERT_ID(),'9a0a7d25af4f7a73f67dde74e8e54cff','football pic 2');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(10, LAST_INSERT_ID(),'c8e60100f13ffe374d59e39dc4b6a318','football pic 3');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(11, LAST_INSERT_ID(),'5e8b6207f007338243d3e29d6b82acab','football pic 4');

INSERT INTO User VALUES ('traveler', 'Rebecca', 'Travolta', 'sha512$1c662feb81e84cd78cf8d6a96e912ebb$eed150f49e6669c4aee79b0f1ed238ec557e8a6dc1af8c8b4dd393a1a6f0926b97bb537fc7a7af95db36982eaa90a313d4968cdc03112321e9dbb3c4aba65337', 'rebt@explorer.org');

INSERT INTO Album(title,username,access)
VALUES('Around The World','traveler','public');

INSERT INTO Photo(picid,format)
VALUES('bac4fca50bed35b9a5646f632bf4c2e8','jpg');

INSERT INTO Photo(picid,format)
VALUES('f5b57bd7a2c962c54d55b5ddece37158','jpg');

INSERT INTO Photo(picid,format)
VALUES('b7d833dd3aae203ca618759fc6f4fc01','jpg');

INSERT INTO Photo(picid,format)
VALUES('faa20c04097d40cb10793a19246f2754','jpg');

INSERT INTO Photo(picid,format)
VALUES('aaaadd578c78d21defaa73e7d1f08235','jpg');

INSERT INTO Photo(picid,format)
VALUES('adb5c3af19664129141268feda90a275','jpg');

INSERT INTO Photo(picid,format)
VALUES('abf97ffd1f964f42790fb358e5258e8d','jpg');

INSERT INTO Photo(picid,format)
VALUES('ea2db8b970671856e43dd011d7df5fad','jpg');

INSERT INTO Photo(picid,format)
VALUES('76d79b81b9073a2323f0790965b00a68','jpg');

INSERT INTO Photo(picid,format)
VALUES('6510a4add59ef655ae3f0b6cdb24e140','jpg');

INSERT INTO Photo(picid,format)
VALUES('28d38afca913a728b2a6bcf01aa011cd','jpg');

INSERT INTO Photo(picid,format)
VALUES('5fb04eb11cbf99429a05c12ce2f50615','jpg');

INSERT INTO Photo(picid,format)
VALUES('39ee267d13ccd32b50c1de7c2ece54d6','jpg');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(12, LAST_INSERT_ID(),'bac4fca50bed35b9a5646f632bf4c2e8','world pic 1');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(13, LAST_INSERT_ID(),'f5b57bd7a2c962c54d55b5ddece37158','world pic 2');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(14, LAST_INSERT_ID(),'b7d833dd3aae203ca618759fc6f4fc01','world pic 3');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(15, LAST_INSERT_ID(),'faa20c04097d40cb10793a19246f2754','world pic 4');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(16, LAST_INSERT_ID(),'aaaadd578c78d21defaa73e7d1f08235','world pic 5');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(17, LAST_INSERT_ID(),'adb5c3af19664129141268feda90a275','world pic 6');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(18, LAST_INSERT_ID(),'abf97ffd1f964f42790fb358e5258e8d','world pic 7');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(19, LAST_INSERT_ID(),'ea2db8b970671856e43dd011d7df5fad','world pic 8');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(20, LAST_INSERT_ID(),'76d79b81b9073a2323f0790965b00a68','world pic 9');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(21, LAST_INSERT_ID(),'6510a4add59ef655ae3f0b6cdb24e140','world pic 10');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(22, LAST_INSERT_ID(),'28d38afca913a728b2a6bcf01aa011cd','world pic 11');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(23, LAST_INSERT_ID(),'5fb04eb11cbf99429a05c12ce2f50615','world pic 12');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(24, LAST_INSERT_ID(),'39ee267d13ccd32b50c1de7c2ece54d6','world pic 13');

INSERT INTO User VALUES ('spacejunkie', 'Bob', 'Spacey', 'sha512$523bbfca143d4676b5ecfc8ee42aca6d$fae41640d635cb42c3631e5a66a997e6f6ebfd25f6bb3f9777107d848c24bd2db9767242e803a881dbc5af73ddbf7ee80d1d855db2568061bfb2ca21fcf2dd5f
', 'bspace@spacejunkies.net');

INSERT INTO Album(title,username,access)
VALUES('Cool Space Shots','spacejunkie','private');

INSERT INTO Photo(picid,format)
VALUES('4ddba6e2f905e9778c6b6a48b6fc8e03','jpg');

INSERT INTO Photo(picid,format)
VALUES('09d8a979fa638125b02ae1578eb943fa','jpg');

INSERT INTO Photo(picid,format)
VALUES('143ba34cb5c7e8f12420be1b576bda1a','jpg');

INSERT INTO Photo(picid,format)
VALUES('e615a10fc4222ede59ca3316c3fb751c','jpg');

INSERT INTO Photo(picid,format)
VALUES('65fb1e2aa4977d9414d1b3a7e4a3badd','jpg');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(25, LAST_INSERT_ID(),'4ddba6e2f905e9778c6b6a48b6fc8e03','space pic 1');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(26, LAST_INSERT_ID(),'09d8a979fa638125b02ae1578eb943fa','space pic 2');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(27, LAST_INSERT_ID(),'143ba34cb5c7e8f12420be1b576bda1a','space pic 3');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(28, LAST_INSERT_ID(),'e615a10fc4222ede59ca3316c3fb751c','space pic 4');

INSERT INTO Contain (sequencenum,albumid, picid, caption)
  VALUES(29, LAST_INSERT_ID(),'65fb1e2aa4977d9414d1b3a7e4a3badd','space pic 5');

