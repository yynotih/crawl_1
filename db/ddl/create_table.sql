create database scrapy;
create user 'scrapy'@'localhost' identified by 'scrapy';
grant SELECT,UPDATE,DELETE,INSERT on scrapy.* to 'scrapy'@'localhost';

CREATE TABLE `cell_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `no` varchar(255) DEFAULT NULL COMMENT '单元编号',
  `name` varchar(255) DEFAULT NULL COMMENT '单元名称',
  `address` varchar(255) DEFAULT NULL COMMENT '单元地址',
  `town_name` varchar(255) DEFAULT NULL COMMENT '所在镇名称',
  `useage` varchar(63) DEFAULT NULL COMMENT '房屋用途',
  `structure` varchar(63) DEFAULT NULL COMMENT '房屋结构',
  `building_area` varchar(63) DEFAULT NULL COMMENT '单元建筑面积',
  `share_area` varchar(63) DEFAULT NULL COMMENT '公建分摊面积',
  `build_base_area` varchar(63) DEFAULT NULL COMMENT '预测建基面积',
  `inner_area` varchar(63) DEFAULT NULL COMMENT '预测套内建筑面积',
  `land_share_area` varchar(63) DEFAULT NULL COMMENT '土地分摊面积',
  `status` varchar(45) DEFAULT NULL COMMENT '单元状态',
  `price` varchar(45) DEFAULT NULL COMMENT '销售参考价',
  `add_date` date DEFAULT NULL COMMENT '记录添加日期',
  `modify_date` date DEFAULT NULL COMMENT '记录修改日期',
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id_idx` (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=83146 DEFAULT CHARSET=utf8 COMMENT='房产单元信息';

CREATE TABLE `house_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `project_name` varchar(255) NOT NULL COMMENT '项目名称',
  `presale_licence` varchar(255) DEFAULT NULL COMMENT '预售证号',
  `company_name` varchar(255) DEFAULT NULL COMMENT '开发商名称',
  `house_num` int(11) DEFAULT NULL COMMENT '套数',
  `land_area` float DEFAULT NULL COMMENT '用地面积',
  `building_area` float DEFAULT NULL COMMENT '建筑面积',
  `presale_date` varchar(31) DEFAULT NULL COMMENT '批预售日期',
  `presale_end_date` varchar(31) DEFAULT NULL COMMENT '预售有效期',
  `add_date` date DEFAULT NULL COMMENT '记录添加时间',
  `modify_date` date DEFAULT NULL COMMENT '记录修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4183 DEFAULT CHARSET=utf8 COMMENT='房地产项目信息';

CREATE TABLE `real_estate_daily_trade` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `town_name` varchar(63) NOT NULL COMMENT '镇名称',
  `trade_num` int(11) DEFAULT NULL COMMENT '签约套数',
  `trade_area` float DEFAULT NULL COMMENT '交易面积',
  `amounts` float DEFAULT NULL COMMENT '交易总金额',
  `add_date` date DEFAULT NULL COMMENT '记录添加时间',
  `modify_date` date DEFAULT NULL COMMENT '记录修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8 COMMENT='房地产每日签约情况';