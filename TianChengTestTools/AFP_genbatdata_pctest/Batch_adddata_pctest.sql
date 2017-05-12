DELIMITER $$

USE `pct_afp_tianchengtest`$$

DROP PROCEDURE IF EXISTS `insert_fraudcheckmodelreq_proc`$$

CREATE DEFINER=`root`@`%` PROCEDURE `insert_fraudcheckmodelreq_proc`()
BEGIN
    DECLARE v_UniqueID VARCHAR(128);
    DECLARE v_ReqJson TEXT;
    DECLARE v_enFraudCheckModelType TINYINT(4);
    #DECLARE v_ReqTime  INT(11);
    DECLARE v_enFraudCheckHandleStatus  TINYINT(32);

    DECLARE UserID VARCHAR(64);
    DECLARE UserIDCard VARCHAR(64);
    DECLARE CardType TINYINT(4);
    DECLARE UserRealName VARCHAR(64);

    #ReqJson_cur_userinfo
    DECLARE ReqJson_cur_userinfo CURSOR FOR SELECT DISTINCT UserID, UserIDCard, CardType, UserRealName FROM  `ubas_tianchengtest.userbasicinfo` WHERE UserID IS NOT NULL AND UserIDCard IS NOT NULL AND CardType IS NOT NULL AND UserRealName IS NOT NULL;
    SET @ReqJson_parttou = '{"FunctionCode":"100122","CurrentTime":"20150723203212000000","MsgBody":{"bank_cart":"12345","reasonno":"04","blackBox":"123","ip":"192.168.1.122","account_login":"test123","mobile_phone":"18675559750",';
    SET @ReqJson_partend = '}}';

    #循环插数据
    OPEN ReqJson_cur_userinfo;
    SET @count = 0;
    WHILE @count < 2 DO
        SET @count = @count + 1;

        # 随机生成UniqueID
        SET @v_UniqueID_r = ROUND(RAND()*(99999999-11111111) + 11111111);
        SET v_UniqueID = CONCAT('abc', @v_UniqueID_r, '123456789');
        SELECT v_UniqueID;

        # 组ReqJson
        FETCH ReqJson_cur_userinfo INTO UserID,UserIDCard,CardType,UserRealName;

        SET @ReqJson_part = CONCAT('"user_id":"', UserID, '","identity_card":"', UserIDCard, '","idtype":"', UserIDCard, '","name":"', UserRealName, '"');
        SELECT @ReqJson_part;

        SET v_ReqJson = CONCAT(@ReqJson_parttou, @ReqJson_part, @ReqJson_partend);
        SELECT v_ReqJson;

        #其他字段
        SET v_enFraudCheckModelType = 3;
        SET v_enFraudCheckHandleStatus = 1;
        INSERT INTO pct_afp_tianchengtest.fraudcheckmodelreq(UniqueID, ReqJson, enFraudCheckModelType, enFraudCheckHandleStatus) VALUES(v_UniqueID, v_ReqJson, v_enFraudCheckModelType, v_enFraudCheckHandleStatus);
    END WHILE;
    CLOSE ReqJson_cur_userinfo;
END$$
DELIMITER ;
