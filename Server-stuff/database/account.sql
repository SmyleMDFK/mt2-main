/*
 Navicat Premium Data Transfer

 Source Server         : 10.5.50.231
 Source Server Type    : MySQL
 Source Server Version : 50651
 Source Host           : 10.5.50.231:3306
 Source Schema         : account

 Target Server Type    : MySQL
 Target Server Version : 50651
 File Encoding         : 65001

 Date: 16/12/2021 09:54:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `login` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '' COMMENT 'LOGIN_MAX_LEN=30',
  `password` varchar(42) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '' COMMENT 'PASSWD_MAX_LEN=16; default 45 size',
  `social_id` varchar(7) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `email` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `status` varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'OK',
  `availDt` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_play` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `gold_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `silver_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `safebox_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `autoloot_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fish_mind_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `marriage_fast_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `money_drop_rate_expire` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `real_name` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '',
  `question1` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `answer1` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `question2` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `answer2` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cash` int(11) NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `login`(`login`) USING BTREE,
  INDEX `social_id`(`social_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES (1, 'root', '*27AEDA0D3A56422C3F1D20DAFF0C8109058134F3', '1234567', 'imerv3@gmail.com', 'OK', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '2021-12-16 11:52:32', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '2021-12-10 07:33:43', '', NULL, NULL, NULL, NULL, 0);

-- ----------------------------
-- Table structure for block_exception
-- ----------------------------
DROP TABLE IF EXISTS `block_exception`;
CREATE TABLE `block_exception`  (
  `login` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT ''
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of block_exception
-- ----------------------------
INSERT INTO `block_exception` VALUES ('NONE');

-- ----------------------------
-- Table structure for iptocountry
-- ----------------------------
DROP TABLE IF EXISTS `iptocountry`;
CREATE TABLE `iptocountry`  (
  `IP_FROM` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `IP_TO` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `COUNTRY_NAME` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iptocountry
-- ----------------------------
INSERT INTO `iptocountry` VALUES ('0.0.0.0', '0.0.0.0', 'NONE');

-- ----------------------------
-- Table structure for string
-- ----------------------------
DROP TABLE IF EXISTS `string`;
CREATE TABLE `string`  (
  `name` varchar(64) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `text` text CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  PRIMARY KEY (`name`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
