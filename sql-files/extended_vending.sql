-- Extended Vending migration for existing rAthena databases.
-- Safe to run more than once.

SET @exists := (
	SELECT COUNT(*)
	FROM information_schema.columns
	WHERE table_schema = DATABASE()
	  AND table_name = 'vendings'
	  AND column_name = 'extended_vending_item'
);

SET @sql := IF(@exists = 0,
	'ALTER TABLE `vendings` ADD COLUMN `extended_vending_item` int(10) unsigned NOT NULL DEFAULT 0 AFTER `sit`',
	'SELECT 1');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
