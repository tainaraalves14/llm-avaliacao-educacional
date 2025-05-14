-- Criar a tabela de questões
CREATE TABLE questoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enunciado TEXT NOT NULL,
    resposta_correta TEXT NOT NULL
);

-- Criar a tabela de respostas dos modelos
CREATE TABLE respostas_modelos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_questao INTEGER,
    resposta_modelo TEXT NOT NULL,
    FOREIGN KEY (id_questao) REFERENCES questoes (id)
);

-- Criar a tabela de avaliações dissertativas
CREATE TABLE avaliacoes_dissertativas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_questao INTEGER,
    pontuacao_completude INTEGER,
    pontuacao_clareza INTEGER,
    pontuacao_precisao INTEGER,
    pontuacao_total INTEGER,
    FOREIGN KEY (id_questao) REFERENCES questoes (id)
);
