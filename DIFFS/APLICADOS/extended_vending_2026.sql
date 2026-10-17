-- Extended Vending 2026 - database migration
-- Compatible with the Extended Vending code used by the rAthena 2026 src.
--
-- The vendings table already exists in rAthena. This migration adds the
-- currency/item ID used by each vending store.

ALTER TABLE `vendings`
    ADD COLUMN `extended_vending_item` INT UNSIGNED NOT NULL DEFAULT 0 AFTER `sit`;

-- 0 = Zeny/default/no extended item.
-- Non-zero values are item IDs configured/selected as the vending currency.
