create table accounts 
(id int(5) AUTO_INCREMENT, 
 name varchar(100) NOT NULL, 
 balance decimal(10,2) NOT NULL,
   PRIMARY KEY(id));

CREATE TABLE `practice_mysql`.`transaction` 
(`id` INT(5) NOT NULL auto increment,
  `type` ENUM('debit','credit') NOT NULL ,
    `amount` DECIMAL(10,2) NOT NULL, 
    accountid int(5), 
    FOREIGN KEY (accountid) REFERENCES accounts(id), 
    PRIMARY KEY(id) ) ENGINE = InnoDB;

INSERT INTO accounts(name, balance) VALUES('ashsih',1000),('vijay',2000.00),('keshav',3000);

INSERT into transaction (accountid,amount,type) 
VALUES
(1,1000,'debit'),
(2,2000,'debit'),
(3,3000,'debit'),(4,4000,'debit');


select * from accounts,transaction where accounts.id=transaction.accountid;

###########################################################
######## Create procedure 1 ###############################
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_account`(IN `p_accountid` INT, IN `p_amount` INT)
BEGIN
DECLARE existing_balance int;
select balance from accounts where id=p_accountid;
END$$
DELIMITER ;

######## Create procedure 2 ###############################

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_account`(IN `p_accountid` INT, IN `p_amount` INT, OUT `p_balance` INT)
BEGIN
DECLARE existing_balance int;
select accounts.balance into p_balance from accounts where id=p_accountid;
END$$
DELIMITER ;

######## Create procedure 3 ###############################

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_account`(IN `p_accountid` INT, IN `p_amount` INT, IN `p_type` VARCHAR(12), OUT `p_previousbalance` INT)
BEGIN
DECLARE existing_balance int;
DECLARE new_balance int;

select accounts.balance into existing_balance from accounts where id=p_accountid;
INSERT INTO transaction (type,amount,accountid) VALUES (p_type,p_amount,p_accountid);

IF p_type='debit' THEN
	SET new_balance=existing_balance-p_amount;
	UPDATE accounts SET accounts.balance=new_balance WHERE accounts.id=p_accountid;
ELSEIF p_type='credit' THEN
	SET new_balance=existing_balance-p_amount;
	UPDATE accounts SET accounts.balance with new_balance WHERE accounts.id=p_accountid;
ELSE
	SET new_balance=existing_balance;
	UPDATE accounts SET accounts.balance with new_balance WHERE accounts.id=p_accountid;
ENDIF;
DELIMITER ;