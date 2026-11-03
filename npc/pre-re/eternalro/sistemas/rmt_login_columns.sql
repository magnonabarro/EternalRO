-- Execute no banco de login; adicionar somente colunas ausentes.
ALTER TABLE `login` ADD COLUMN `nome` VARCHAR(100) NOT NULL DEFAULT '';
ALTER TABLE `login` ADD COLUMN `cpf` VARCHAR(20) NOT NULL DEFAULT '';
ALTER TABLE `login` ADD COLUMN `chave_pix` VARCHAR(100) NOT NULL DEFAULT '';
