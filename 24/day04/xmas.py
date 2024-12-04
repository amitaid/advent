
from collections import defaultdict


ex = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

data = """MMMMASXMMMMXXMASMMXSAMMMSAMXSXMMXMXMXAMAMXSXXXMXAXAMXMMXAASAMXMSMMMSXSAMXMASAXXAMXAMXAXSXXMASXMMXMASXMAXXMASMMMMXMXSMSSSXSASASMSAMXXSMSMSSXS
MAAXMXMAAAMSMSXSXSMSAXSXSXSASAXAASAMXXSMXXMASMMSMSXSAMSMSSSMSMMAAMASMMAAMAMXMASXMSAMXSMSAAMASMXSASAMAMAMXSAMAAXMASAMASAMXSASASASXMAMSAAAXAAX
MSSSMMSSMMSAASAMAXAMAMSAMAMASAMSMSMSMMAAMSAMXAXAAAAXXXAAXAXXAXSSSMXSASXMSXXASXXAXXAXXMAMXXMASAXSASXSAMAMAMXSSMMSASAMXMMMMMAMAMAMMXSAMMMSMMSM
XMAMAAXXMMSMSMAMAMSMMMMAMXMXMAMMASASASAMMXAAMMAMSMSMMSMXMMMMMMXAMXXSAMXAAMSMXMMMMSMMSMAMXMMMMAMMXMASXSAMXMAAAXAMMMAMMXXAAMAMAMSMSAMXSXXMASXM
MMAMSXSAMAMXXXSMSMMAXSXSMASMXAMMAMAMMSASXXMMSSMXAAMXAAXMSXMAXXMASMXMAMMMMAAMAAAAXXAAMMAMSXXMMASMASMMXSXSAMXXSMSSSSMMAXSXSSMSMSAAMXSAXMAMSAMS
XSXMAXSAMASXMAXAXASMMSAAMAMXSMSMSMMMAXMMMXAAAXXMMAMMSMSASAMSAXXMMMMSAMAAXSXXMMXSMMMMSMSASAMXSASXMXAMAMASXMSXMAMXAAXSSMMAAXAMXSMSMMMMSMXMAMAX
MMAMMXMXSMSAMMMMMMMAAMSMMSSMXMAMXAAMXXXMAXMMXMXAXXXXAAXMXAMMMMXMXXASASMSXMMMSMMAMXSAMAMMXMAXMASMMSSMMMASASMSMAMMSMMMAAMMMSXMMXXAAAAMXAAMMXMS
ASXMXXMASXMAAAAAAXXMXMMXMAAAMSAMXMMMSAMXSMMASMMSSSMSMSMXSSMSASMAMXXSAMAXMASAAASMMAMAMXMMAASAMXMMMAAAXMAMMXAASAXXAAASMMMXAMASXSSMSMSSMXASAAMA
MXMXXAMXMASXMSSSSSMXAAXAMMMSMSASXAAAMSMAMMMAAMAMMAAAAAXXXAAXASAAMXAXAMAMXAMMSMMAMXSAMMMSSSMXXSXXMSSMMMSSMMSMSMSSXSMSMMMMMSAMAAXXAAXAXXAMXSSS
SMASMXMXMXMSAMXAAMMSMXSAXXXMASAMMSMSAMXAMXMXXMAMMMMMSSSMMMXMXMXAXXMSMMXSMXSXMXSMMMAMXMMAMAXMAMSMXMAAXMMAMAMMXMAXXMAXXAAAASAMXMMSMXSAMMXMXMAM
AASAMASXMAAXXSMXMAAMMMXAXSXMAMAMAXAXMASXSASXMSMSAAXMXMAASAASMSSSMAMAXMXXXMMXMMMAAMASMAMASMXXAMAMAXMMMMXAMAMXSMAXXMAMSSSSXSXMXSMXSAMXMMSMSMAM
XSMASXMASMXMMXMASMASXSXSMSAMXSMMSMMMXMMASMSAAAAMMMMMAMSMMASMAAAAXAXMXMAMXXSAMXXSASMSAXSAXXSSMSSSMSMAAMXMMSSMMMSSXMXMXAAMAMXMXMMASMSMMASMMMAX
XMAMXASXMSMAAASAAMAAMMAMMXMMAXMAAASXSAMXMAMMMMSMMXMMAMASAXXMMMMMSSMSMSAAMASMSAMXASMSXXMMSMAAAAAXAAMSMSAAXAAASAASAMXMMMMMMXAMAAMAMXXAMAMXXSAS
XMAMXMSXAAMMSXMAXMMSSMXMAAASMSMMSMMAMXSXMMSSMAXAMAMSMSAXXSXXXSAMXMAAXSAMSAMXAASMXMASAMAAAXMMMXSSSXXMASMSMSSMMMSMXMAXAMXAASMSSSMSSSMMMSSMAMSM
XSASXAXMSMSAXMSSMXAMAMMMMXXAASMMMAMSMAMAXXAAMASAMMMAMMASXMXMAAAMAMMMMMAXMASASMMMMMMMASXSXMXAXMMXXXAMXMAXXXAMSMMMAMSMSAMXXXAAAAAMAXASAMXMAXAM
MSASMMMMMAMAXXAAAXAMAMAMASMMMMAASAMXMASAMMSSMXSMMSMMSMAMAAMMSMSMAXXMMMAMSAMXMAXAAMXMAMMMASXSMMMASMMMAMXMXXMMAAASXSMAMASMXMMMSMMMAMMMMSXXSSMS
XMAMXMAAMSMSMMSSMMMSSSSMAXXMASMMSXMASXSASXAXAXMXAXASAMXSMXMAMMAXSXSASXMXAMXMASMSSMXMMMAMAMAAAXMAMSAMXMMSXASXSXMMXAMXMAMMASAMXMXMMSXAMSAMXAXA
SMXMASMSSMAMXXAXAXXAAAMMMMASASMMMMSMSMMMXMMSXMMMMXMMMMMMMAMMSAMAMAAAXAMSAMXSAMAAAASMSSXMAMXSMMMXSASAXMASXMMAMSSSSMMMMXMAMXMAXMXSAMMMXMAMSAMM
XAASASAMXMAMXMASXMMMSMMAMSXMASMAMAAMMAAXMAMSXXSAMASAMAMASXSAXMXMMXMXMXMAASXMASMMMMMAAAXSASXXAXASAAMXSMMSAXMSMAXMAXASMSXSAMXXMAAMASXMXSSMSMMX
MSMAAMXMXSMSAMAMMMSAAXMAXMASXMMAMMMMSXMMSXXMAASAXAXAMAXXSXMASXSXMSSMMASMSMMSAMXSXMXMMMMSASMSXMMXMXMAMXASXMMMMXMSAMXAAAAXSMASXMMMMMMMXMAXSASX
AAXMXMMSAMASXSASAAMSSSSSMSASASXXXAXXMSSXMXAMXMSAMSSMSSXMMAMXMAMSAAAASASXMXXSAMASAAXXXSAMXMMXMXSXMAMASMXSMMMAMAAXSMMMMMXMAMASAAMSMAAXSAMXSAMS
SSSXASAAAMMMMMAMMMXMXAAXAXXMAMASXSMASAMAASXSAXMAMXAXAAASMSMMMMMMMMSMMXSAMMAXAMASAMMMMMAXMMMXAASASXSASAMXMAAAMMSMMMAXXXAXMMASMMMASMSMMAXXMAMX
XAAMAMMXMMAASMSMXMXXMMSMMMSMMMMMAASMMASXMAMSMSSXMSXMXSMMAAMAASXSSMXXSASAMXSSMMASAMAAMMMMSASMSMSAMMMXSMMXSMSSSMAAASXSASASXMMSASXMSXMASAMMSSMM
SMMMXSMMSXSAMXXAASASAMXAMAMXAAAMXMMXSAMXMAXXMAXMXSMMMMAXMMMSXSXAAASAMXSMMMXAMMAXAMXMXSSMXAXAAXMAMASMMASXMAXXAMSSMSXSAMSAMXXSAMMXSASAMMSMAAMM
XAXXXMXAXAXMASMSMSASMXSMMSSSSSXXAXXAMASMSMSASMXSAMAAASMMMSXMAMXXMMMAMXMAMASAMXSSSMXSAMAAMSMSMMXAMSMAXAMAMAMXAMXMAXAMXMXXMMXMMMSAMAMASASMMMMM
SMMXXMAXMMMSXSXAXMAMMMSAMXAAXMASMSMMSAMXAAXAMXMMASXMXSAAXSAMXMASXXSMMAMASMSXAXMAMXAMASMMMAAAASMMMASXMSSSMMSMSMAMXMXMMSMMMXXAMAMXSAMXMAXAMAXX
SMASXMSXSAMXAMMMSAMXSAMAMMMMMMMAXMAMMMMMMXMXMXASMMXSMMMMXSAMXMXSXAMASASMSASMSMMXMMXXMMMXXMMMXMAMSAMMXMAMXAMXAMMXSAASAMAAASMSMASASAMAMXMSMMSA
XMASAAXXSMSMXMAMAMSAMXSAMXMASAMMSSSMAAMSASMSSMXSASMSXMAXXXASXMXSMXMMSASAMAMAAASXMMMMSAMMXSAMXSAMMSMMSMAMSAMSMMSAMSMSASMMMSAAMAMXSAMSMSAXAAXM
SMXSMMMXMSAMXSXMAXMASASMSMAAXAXSAMAXMMMXAMAAAXASMMAMMSMSSSXMASAXAASXMAMMMXMXMSMAAXAASAXSASAXAMAXAMXAMMAXMAMXMAMXMXXSXMXXXMMSMSSXMXMAAMASMMMM
MMMMAMMAMMXSXXXSSXSAMASAAMMASMMMASMSXSAMXMMXMMAMXMAMMAAAXMASXMXMXAMAMXMASMSMMAXMMMMXMMXMASMMSXSMSMMSSSSXSMMSMSSMMSMSMMSXXMAXAMAMSMSMSMMMMAAM
MAAMAASXMSAMAXMXAAMASAMMMSSXMAASXMXXAAXMXSMASAXXSSSSSMMMXMMMXMXMSSSMMXMASAAASAMMXMMMMMAMMMXAXAMAXXAMXMMASXAXSAAAXAXMAMAAMXMMSMSAMXMXXXXASMMM
SSSSSXXAAMXMAMAMAMSXMAMXMAXAXMMMSMXMXMMAXAMXXAMXMAAMMXSAASAMASXAAAAMMSMAXXXMMAXSASAAASASASMXSXMAMMMSAXMAMMMMMSSMMMXSSMXXMAXAXXAMSMSMMXSXMMSS
XAAAXAMXMSSSSSSSMXSMSMMAMMSSMMSMMXAMXMXXMMSSMASAMMMMXAXSASASAXMMMSMMMAMMMSMMMXMSAXMSMMASASAASMMXMXASMMMSSXSAMXXXAXAMXMAASXMMSMMXSAAAMXMAXAAA
MMMMMXAMAMXAAMASMAMMAASXSAAXAMXAAXXSSSMSMXAXMAXAXMXSMSXMXSAMMXSAAAMASMXSAAXSXXXXSMXXAMMMMMMMXASMSMMSAXXMAAMXMXMAMAAXAXSXMAMXAAXAMSSSMAXSMMSS
SSSMSMSSSMMMMMAMMASMMMMAMMSSMMSMMSXAASAAXMASMSSMSSMMAXXMAMAMXASMSXSXSAAMSSMMAMMAXMXMAMXAXXXMSAMAMSXSAMXMMMMSXMMSAXSMMMXAXMASMSMXXXXXMSXXAXAM
AAAAAAAXMASMSMXSMMSAMSMMXAMAMAMAAXMMMMSMSSMSAXAAAXAMSMSMXSAMMMSXMXSAMMMMXMAXAXMAMASXSMSSMAAXXSMMMMMXMXAMMSAMASAMMMXASMSSMMASAXASXSAMXMASMMXS
SSMMMMMXMMMAAMASXMMAMXAMSMSAMASMXSASAAMXMAAMXMMMMSSMAAMAASASXXMAAAMAMAXXXASMMSMXSAXAAAAMMSMAAXMXAMSMSMXAAMASAMAAXXSAMAAMAXXMASXMAMXMAMXSAMXA
MXXXXXASMXMSMMAMAXSAMMAMMASMSMSAAXAXMSAASMMMMSXXMAMMMSMMMXAMMXSXMSSMXAXXXMXSAAMAMXSSMMMSAMXMSMXMASAAAAMMXXXMMXMMXMASMMMSAMXMAMAMXMAMXSAMAMSM
MAMMSMXXAAMAMMMMMMMAMMMXSAMXMAMMMSSXAAMMXAXMASASMAMXSXMMSMMMAAMAMAMMMMMSAMAMSMSSMXAXAXXMXSXXMAASXMMSMSSMSSSMMXMXXMAAMXXMAXXMASAMASAMSMMSSMAX
MASXMSSMMMAAXAAASASMMASXMASXXAXAMAMMSMSMSAMXSMAMMSMXMASAAMASMXSAMAMAAAAXAMAMAXXAMSASXMXMMMMMMSMMAAXMAMXAAAAAAASMMMASXASAXSASASASASAMMAAAAXXA
SXXAAAXAAXMMSMSXSAAAMXSAMMMASASXMASXAXAXAXMXAMXXAMMAXAMMXXASXASASMSSSSSSXSXMSXSMMMAMMMAMAAAXAAAMXMMMAMMMMSMMSXXAXMAMAMMAMXAMASAMMSXMSMMSSMMA
MSMMMMXSMMXMAXXMMMMXMAXAXMMXAXAASAMMMSSSMSSSXSAMXSSSSSSXSMASXXMASAAAAAMXAMXAMAMXMMAMXXAMXXSXSSSMSXMMXXXXAMXAXXMSMMMSAXMAMMXMXMAMMXMMXAMXAAAX
AXXSAMAXAXSMMMSAXAAAMXSAMXXSMMXMMXMAMAAMAAAXMMAXXXAAAAAASAMXMXMASMMMMMMSAMMXMAMASMMAXMSSSXMAMXMASAASXMSSSMMSSSMXASASAMXSSMMSXSXMXAMMSSMMSSMS
MAMMASAMAMXAXASMMMMMXAXMASAMXMAXXXXAMXMMMMXMMSAMXMMMMMMXMXMAMXMASXSXXSASASASMSMASAMXSXMAAAMSMMSAMMMMAAAAAAAAXAASAMASXMAXAMASXSMMSASAAXMMAMMA
MAMSAMMSSMSSMASMSAMSMSMSXMAXAXMSMSSXSAXXAASAMAXSAAXXMXSXSAXAXAMASMSAMXASAMAXMAMMSAMAMXMAMXMASAMAXXXXMMMSMMMSSMMMXMMMMMXSAMXSAMAXSAMMXXAMAMXM
SAMMXMXMAXAXMXMAMASAAAAAXSMSMSMAAMAASMMMXMAMSAMSMXSAMAMXSASXSXSAMMMXMMXMAMMMSMSMSMMASMMMMMSASXSXMSMMSAXAAMAXXMAMAMAAASMMAMAMAMSMMAMMAMSXSSSX
MXMMMMSMMMSXMAMXSSMMSMSMAXAAAAMMSMMMMAAAMXAXMAMXMASXMASASXMAAXXAXSXSXMAMXMAAMXXAXXXXSAAMAMMMSAMAMXAASASXXMMXXMASAXMSMXAXXMMXXMAASAMMAMMAXXMX
AMMSMMAAAAXXSMSAMAAMXAMXAMXMSMSXMAXMSSMSAMMXSAMXMASASASMMAMXMMMMMSAMXSASASMSXSMMMXSAMXMSAMAXMASAMMXMXXMMMMSMAMAXMMMXAXSMSMSSSMSMMMSXMXMXMASM
SAAAAMSSMSSMXMAXSSMMMSMMASAAMASAXXMXAMXMMSAASASXMXSASAMXSAMAXAXAAMSMAMMSASXMASASASMMSAMXMSSSMASASXSMMASXAAAXAMSMSASMSMXAAAAASAAXAXSXSASASAMA
AMSSSMAAAXXAAMXMXMASXMXMASMSMAMMMSXMASMMASMASXMMSMMAMAMXSASXSSSXXXAMXXMMXMMSMSAMMSAMMAMSAAMAMASXMXAASAMXMMSSSSXASAXAAAMXMMMXMMMSSSMASASAMXSS
MXMAMMSMMMMSMXMSMSAMAMXMASXXMXMAAMAMXMAMAMXXMASAAMSASXMAXAXASXMMSSMXMASMMMMSAMXMAMMMSAMSMXSAMXMAXMSMMASMSXMAMMMMMAMSMSMXXMMMSXMAMAMXMMMXMAMA
XSMXMMMAXMMASAAAAMXSXMSMASASAMSMSSMXAXXMASMSXMASMXMASMXSXMMMMAMMXAMXSASAAMAMAMAMSSMAMAMXAXSMXSXMMAAAXXMAAMMMMSSXMXMXAAMXMXAAXAMASMMMAXSXMASM
SMMSAASAMXMAMMMMSMXMXAMXAMMMXAMXMAMSMSASAXAXAAMXXSMAMMAMAMASXSASMSMXMASMMSASXMAAMAMASXMMMMMAMXASMSSXMMSSMXXAAAMAXSMMSMSAASMSXXXAXMAXMMMASMSX
XASMMMSMSSMMMSASAMASXMMMMSSMXSMMMAMAAAXMMSSSMMXXAMMSMMAMAXXSAMMSAMXMMMMAXSASMSXXSAMXAASXMAAAMXSMAAAXSAMMXXMMMSSMMAAXAASXMMAAASMSSSSXMASMMMSM
MMMMAXMXAAXSASMSASAXXMMAMXAXXMAXSSSMSMXSXAXAMXMMAMAXMSMSMSMMAMXMAMMMAAMAMMXXAXAXXXXAXMMAMMSASXAMMMSMMAXSAMXAAXAASXMMMMMXSMMMSMAAAAAMSAMAMAMA
AAAMXMMMSSMMASAXXMMSSMSASMMMMMSMAMXMAMAMMMSMMASMMMSSXAMAAAAMSXXXAMASXMXAMXAMSMSMMSMSAXSAMMXAXXXMXXXXSMMMMMSMSMMMMAMXXASAXMAXXMMMMMMMXASMMAXS
SSMSAAMAMXMASMMMMAXAAASMSMXXXAAMXMMSAMXSAXMASXSAXAAMXSSMMMSSMMSMSXXMAMSMMMXMMAXAXAAAMMSAXXMMMMMMMMAMXMAAAAAMAXXAXXMXAMMASASMXMAMSXMMSMMMMMMM
XAASMMMSMMXSXMXASXMMSMMMMMSMMSSXSAASASMMMSSXMASXMMXSAXMXAMXAAXSAMXSMXMAMAMMXMASXMMSMXAXXMSXSAMAAAXAAASMSMSMSASXSSMAMAXSMMAAAAXAXXMMAMXAMASAX
MMMMAMAMAMMMAMXMSAAAAAAMAASAMXAAMMMMMMAAAMMXXAMAXXAMXSAASASMMAMAMASASMMSASMSMMMMMXMXSMSMMXASAXSSMSSSMSMAMAXMXSAAAAAXSAMAMXMSXSSXSAMASXMSASAS
MAAMXMASAMSSXMSXSXMMSSMSMSSSSMMMMASXSSSMSSSMMMSMMMXSAMAMXAXMAMSAMAMAAAASXSXMAAMXSAMAXAAASMMMSMXAAAMAXMMAMXXSAMXMAMMMMASXMMXMAAAAMMSASAMMASAA
SXSXXMXMXMAMMAMXSAMXXAXXXMMAXMASXAAXMAMAXXAMAMAAAAAMASXAMXMSAMXXSXMMMMMSMSASMMSAMASXMMMXMASAXXSMAMSXMMSMSMAMXSAXXAXXSAMXAXAMMMMMMAMMSAMMMMXM
AAMMXSSSSSSXMMMXXMMMSXMSXMMSMMMAAXMMMSMXMSXMASXSMSXSMMMAAAAMMSSXXAXMAMXMASAMXAMMSAMMSAXAXXMXSAMXXXXAMXAAAMAMMMMMMSSXMASMSMXSMXSXMASASMMXMAXX
MAMMAMAAAAAMSSMMXSAAXMXXASAMASXMSAMXAAMXAXASAMAXAMMXAAMASXSXAAMXSXMXXSMMXMASMMMAXASASASMSXMMMMMMASMSMAMSMSASAAAMAXMAMXMAMMMMMAMAMMMMSXSAMMSS
XSAMXSMMMMXMAAAMAXMXMAMSMMAMMXAAXXMMSMSXMSXMASMMXSXSMSSMXAMXMASMMMXSAAAMASXMAAMMSMMMMXMAAASAMASAASAMAMMMASXSMSMSMSSSMXMXMAAXMAXAMXAXXXMASAAM
MMXMAXXXXMAMMMMMMSMSXXAAXMXMASMMMXMAMASAMAXXXAXMXMAMSMAXMAMSXSXXAAAXMXMSASASMMSXSXSXMXMMSMSASASMSMMMAXXMAMXSAMASXAAMMMMAMXSSMMSASMMSMMSAMMSM
XSAXSSMXASXSSSXSXAXAAASMXSAMMMXASXMXSMSASMMMSMAMAMAMASAMXAMXXMASMMSSSMXXAXAMAXSAMAMAMXSAMXMMMMSXXAXSMMMMMSMMAMAMMXMMXASAXSAXAAXAMXXAAAXAXMMM
MMMMMAAMXMXAAAASXMMMSMMAXMAXXXMMMAXAMXSXMAAAAMASMMASAMXMSXMAMSASAAAXMASMMMSMMXMAMXMAMAMMSAMSSXMAMSMSAAXAAAAMXMXXMXAMXXMASMAMMMMSMMMSMMMSMMAS
AASASMMMSMMMMMSMAXSAMAMMMXXMSMSASAMXXXMASMMSMMASAXXMXSXMAMXXXMASMMXSMMMAAAXAXXSSMMMAMXSASXSAXMXMXMAXXMSMSSSMXMMAMSMMXMASMMMMAXMAASAAASXMASAS
SMSASXAXAASXXSAXXMMASXMSSSMMSAAAXSAMMMXAMXMMMMASMMSAXAMXMMSSSMMMXSSMMAXXMMXAMMMAASXSMAMMSMMMSMAMSMSMSMXAXAMXMMXSAAAMSAMXXAXSMSSSMMMMXXASAMXS
XAMAMMXMXAMXMXAMMMSXMASAAAAAMXMSMMSMASXMSXAAAMXMXAMAMXSXXXAAAXSAMXAASXSSSXSASXSMMMAMMMMXXAAXAMAMMAMAAAMSMMMSMMAMSSSMXAXAMMXXAAXMXXXSAMXMAMAS
MAMSMMXSMSSMSMXMAXMMSMMMSMMSMSMXASAMMSAMAAMXSSMSMSXXAXMASMMXMMAXSXMMMXXAAASAAASXSMMMAXXMMSSSSSSSMAMSMXMXASASAMXMAXXMSMMMMSAMMMSAMXAAXAAMXMXM
SSMMXSAXXXAASXSXSAXMAXMAXMMAMAMXMSASASAMMXMAMAAXAMMMSSMASAMSSXMASMSSXSMMMMMMMMMAMSXSMMSAMAMMXAXXXAMAMXXSMMASAMSMSMMMMXAXMXMSXXXMAMXAMSXMASAM
SAAAAMXSMMMMMAMAXMMXMSMXSAMASASMXXAMXSXMXAMMSMMMAMAAAXMAXAXAAAXAXXMSAMAAMSASXSMSMXMXMAMSMASXMSMSSSSMMXMAAMXMAMXMASAAMMSSMAMMAMXMXAXSMMXMASAS
XSMMSSMMXMAMMMMSMXSAMXMMMXMASAXXSMAMAXMASMMASAMXXSSMMMMSSMMSSXMASMMMMMSMMSAXAXMASAMXMASXSMMMMMAXSXAAAXSXMMMXAMXMASMXSAAAXASAAMAMMSMMASXSXSMM
MMMSAXAAAXAMAAXXAASAMMMXAMMMMMMAMXAMXSSXMAMASAMMAMAXXSXMAMAXMASAMXAAXXXMMMSMAMSASMSXMMSAMXAAAMXMMSSMMXMMSAAMSSSMAXMAMXMSAMXXSSXSAMASAMAXAMXS
AAXMASMMXSMSXSXMMMXAMXAMSSSMAXMAMSXMXMMMSMMAMAMXAMXMMAMMAMSXMXAMXSXMXXXXAAXMXMMASAAMMMSMSSXSSSXSAAXASASASMSMAAAMSMMXSMSMASMMXMXMASAMMSMMSMMX
MAMMXMAAXSAMAMAASXSMMMXSMAAMMMMAXSXSAAAAAAMSXSMSSMSAXMMSSSXASAMXXMAMSMMMMSMMASMMMMMSAAXAXXAMAMXMMSMXXAMAMAMXMSMMAASASMAXAXXMASXSMMMSMAMAXAXX
AAXAAXMASMAMAMXMAMXAAMXSMSMMMSXMAXMASMMSMSMXAAMSAAMSMXMAMXXXMAMMMSXMAAMSMMMSAXSMXSASMSMXMMXMAMXSAXXAMSMSMSAMXAAMSSMAMMSSXMAMXSAMSMXAMASXMMMS
SASMMSMSMXAMSSXMXASXXMASMXAMXSAMXSXMXXXAXMAMXMMMMMMMMSMMSXSSSSMAMAXSSSMSAAMMSMAXXMASAXMASMMSXMAMASMMMXAXMAMMMSMMXXMAMAXXMXSSXMXMAMMMSXSASMAX
MXSXSAMXMSSSMMMSMMMSAMASXMASAMXMAMAMMSMSSMAMSSXSASXMAAMXSAMMAXSXMAXAAMASMMMAMMXMMMMMMASAXAXAMMAMXMASAMSMSMMSAMASMMXSMMSAMAMMMSASASAMXAMAAMXS
MAMXMASXAAMXAAAAAAAXMMXSXXMXMMSMMSAMMMAAXXXMASASASAMSMSAMAMMXMMMASMMSMAMAMMASAMXAAXAMMMSMSMMXSXSXSAMASAAXAAMAXAMAXAXAASAMMXAASXMASXXXXMXMAMX
MAMASMMMMMSMSMSSSMSMSAMMMXSAAMAAMSXSAMMMSAMXMXMMAMMMXAMXSSMXXAXAAMXXAMSSSMMAMXSXSMSASMAXMXAXAMAAAMASMMMMMMMXAMSSSMMSMMSAMXMMXXMSMSASXSMMXSMM
SXSXSAAXMASAMMMMXAAAXMAMSASXSSMSMXXSASXSMMMSMMMMXMXAMAMMAMMMSSSMSSMSMSMAXSMXSXSAMAXXAMXMASMMMSAMXMXMASXSMXSMXSXAXXMAMASMMAASMMAAAMMMAASAAXAX
AMMXMXMMMASMSMSSMSMSMMMXMAMXXAMAMXXMAMXAAAAAXAAAAMMMMAMXAXAXSXAXAXXAXAMMMXMMAAMXMAMXMASMAMAAAXMXXSASMMAAMASXSAMXMMSAXXMAXMMAASXMMMAMSMMMMSMM
XASMSMXAMXSXMAAXMAAAASXMMAMSSMMAMMMMAMMSSMSSXSXSXSASAAMSXXXSMSMMMSSMSXSASAMAMXMMMXSXSXMMSSSMSSMSMXASXMXMMASXSMSAMXSXSSSSMMSSMMASMMXMXAXXAAXM
MSXMAMSMSASAMMMSSMSMXMAAMMXMAMSAXAASAMAAXXMMAXAMASASXSXMSAMXMAXAMXMXMASMSAMAMAMSMMAMMSMAMXXAXMAAAMSMMMSXMASMXASXSAMXMAAAAAAAXSAMXMSAMXMMSSSX
SMMSAMMAMASAMXXXMAXXXSMMMSMMSMSASMMSAXMASAXXAMAMMMAMMMAAXXMAMMMAMAMMSMXXSAMXSASASAMAAAMAMMXMMMSMMXAAAAAXAXXAMXMAMMSXMMMMMMSSMMMXSAMMSMXXXAMX
AMASMMMXMXSAMXXAMSSSMSAMASAAAAXAXXXMXMXMAXMMXMAMXMAMAMMMMASXSSSSXMSAMXMXSXMASXSMSSXMSSSXSXAXAXXASXSSMSSXXAMSASMXMMAMXAMASXAMXMAAMASMAMMSMSMS
MMMMAXSMXMSXMSXMXAAMASMMASMMMSMSMSMSMMMMSXXAMSSSMSSSMXAAMAMMXAAAASMMMASXMASXMASXMASMXAXMMXSSMXMAMAAAAXMMSXMAAMXAXMAXMASAXMMMAMMMSAMMAMMMAAAX
XSXSMMAASMMXXMASMMSMAMXMMSXSMXAAAAXAMAAXMASMXAMAAMAAXSXMMAXAMMMMMMASMMSASASAMAMAMMMMMXMXXAMAMSMAMMMMXMAAMASMSXMSXMXSAXMXSAASASAMMXSSMSSMSMXM
MXXSXMSSMAASMSAMAAAMXSAMAXAXAMSMSMSMXSXSXAMXMASMMMMMMMASMMXSAAMSMMAMAASXMAXMMMSMMMAXXMAMMMSAMASMMXXXAXMMSAMAMMAXMSAMXMAXXXMMXMAXSAXMAXAAXAMX
ASMSAXMAXXMSAMXXMMMMXMASXMMMXMAAAAAXMMAXMMSSSMSAXXAXAMAMAAAMMXMAMMMSMMMMMSMAAAAAAXXMXMSAAASXSASMSSSSSSSMMMMAMMMSAMASAMSMSMSMMSSXMASMSMMMSAMX
XMASAMXAMMXMMMMSSMSXMSMMAXSSSSMSMSMSASAMAXAAAASAMSSSMMSSMMMSMMSXXAMSXAXMAMMMMXMXMMSXSAMXSMMAMASAXAAAAXXXAASMSAXAMSAMMXAAAAMMAXMASAAAAAAAMAMX
XMXMMXMASXMXAMXMAAXSAASMXMXXAAAAAXAMAMAMXSMSMMMAMAAAXAXAMXAAAMAXMAMSMSAMXSASXMMSAXAAMAMMMAMAMMMMMMMMMMSMSXSAMMSMMMASXSMSMXMMXSSXMMSMSMMXSMXS
XXMASAXAXAMSAMXSMMMASMXXAXXMMMMMSMXMAXAMXMAMXXSMMMSMMXSASMMSSMASMSMSAXXSASMAAAASMMMXMXMASXMMMAAAAXSAXAXMMAMXSXMXAMMMAAAMAMSSMMXMAMMAMMMXAXAM
MMSXMAMXSAMXAMAXXXXMXSXMMAMSXXXXXMMSMSXSAMSMXMAMXMMXSMMAMXAAXMMMAAAMSMSMAXXSMMMSXAAXXXSXSMMASMSSMSMSMMSAMXMMSAMSMSSMSMMMAMAAXSASAMXAAAMSMMXS
SASAAXAXMAMXXMSSMMSXAXMASAAAMASAAXAAAAXMXMXAMXMSAXSAAAMSMMMSSSMMMMMMMXMMAMXXMASXMXSSMASMMXSASXAXMSAMXMMXMAAASAMXAAXAXAXXAMXMMSASASMSMMXAASMS
MASMMXSXSSMMXXAAAAMMMSAXSAXXSASMMMSXSSMAAXMSMAMSASMAMXAXAXXXAXXAMXMMMAMAMMSASXSAXXAAXAMAMAMASMMMAMMMMXASXMMXSAMMMMSMSMMSSMXXMMAMASXMXXMSSMAS
MMMMMXAAAXMASMMSMMSAMMXMMXMXMMMXMAMMMAMSMMAMMXMMXMMAMMSSMMMMMMMMASAMSASMMASAMAMMMSSMMSXXMMSASAMSSSMAMMXXAXMAMAXXAAAAAXAXAAASXMMMXMASXMXXXMAM
MAAAMXMMMSAMXAXAXAMASAXSAMXXMMSSMXSAXAMASMMSMMXMMAMASXAAAAMSXSASMMAXSAXAMXSAMMMMXXAAAAASMXMASAMAAMXAXMASMMMMSAMXASMSAMXXXMMSAMXXASXMXMAMMMMS
SMSSSSXSXMMXXSMAMXSXMASMSMMMSAAAAXXMSASASXAAAMXSMASMXMSSMMXSASASXSMMSMSSMASAXSAMXSMMMMSAAAMMMXMMSMSMMSAAASAMXAMXAMMMXSMSXMAXXASMXXXMAXAXMAMS
AXMAXMAMXSSSMXMXMMMMMXMAAXMASMSMMMAMSXMASMSSSMASMMMMMAAMASXMAMAMAAMAXMAAMXSAMSAMXAAAAXMMAMXSASXXXAXMAMMMAMXSMAMAXMAMAAAAAMSSMMAASMASXSXMXAXX
XASXSMSMAMAAAMMAAAMXMAMSMSMMXXXAXXXMMAMAMAMAAMXSAMAAMXMSAMXMMMAXSMMSMMSSMAMAMSXMXXXMXSSXSXXMAMAMMSMMMSSMMXMAMXXSSMSMAMSMXMMAMXMASMXXAAMSSSSM
MXMASAMMASXMMSSSXMSMMAMMASMMMSSSMMMMSAMXXMAMXMASAMXSAMMXMASMASXMMXXAXMMMMXSSMMMMXMMSXMXAMXXMAMXMAMAMAAAXSAMXXMMMAAMXSAMXAMXAMXXXMXMMMMMXAXMA
AASXMAMSMMAMXXAAMSAMMSSMAMAAAMAMAMSASASMSMSAAMASXMAXMAMAMMMXAMASXSSMMSAXXMAMXMASMMAMAMMXMAMXSAAMXSAMMSSMSASXAAASMMMAXAMSSSXXSSMMMAXAXXSMMMAS
SASAMMMASMAMAMMMMSASXAAXSSSMXSASAMMASASAAAASXMASAMASXSSMXXAMSXMMAAMAAMMMMMSMMMSMSMASAMMSMASMMSASASXSXMAASAMXASXSAAMMXAMSXSAAMMMASASMSMXAAAMA
MAMMMXXAXSAMXMASXMAMMSMMMXAAAXXMAMMMMAMXMXMMMMASXSMSXMAMAMSXXAMMSMMMMXSAMAAAASAAASMSXXMASASAMAXMAMXMAMMMMAMSXMASXMXSSSMSAMMSMASMSASASMSSXSMM
MSMSASMMMSMMAMXXXMAMXMASXAMMMSMSXMSAMXMXSXAASMMSAAMMASAMXAMASXMAMAMXMASASXSMMMMSMMXMAMSAMMSAMMAMAMASAMXASAXSAMMMMSAMXXAMSMAAXXSAMMMASXAAMMAX
XMXMASXXAXASMSXMASASXMASMXSAXAAMSASASMSAMSSMMAXMXMAMXMXSMXMAMAMXSAMXMASXMXXAMXXXXSMSAXMASAXAMXXSSSMSASMMSXMMXMXAAMMSAMXMXMSMSMSMSXMASMXSASMM
XSASXXMMSMXAMXMAMSXSAMAXMAMXMMSMMXSXMAMXMAMASMMSMSXMSAMXAXMAXXMASAMXMASMSAMXMMSAXMASMMXXMASXMSMMAAXXXMAAMAAXAXSMSXXXMAMXMXMXSASASXMAMXMAXXXX
MSAXXAMXMSAAAXASAMXSXMXSMMSMSMMXMXMXMMMSMASMMMAAAMAMXAXSSSSMSMMXSAMSMMSAMAMXSAMXMMMMASXMMMAMXXAMMMSSMMSASXMXMXAMAMSMSSSMAAMXMAMAMXMASMXMASMX
AMXMXSMAXAMAMXXMASAXAXMAXAAXAMMAMAMAMASAMAMAAXSMSSXMSSMMAAXAAXMAMAMXAAMMMASMMXSAMXAMAMAAMASMMSSMXAAXAMXXMASAXXAMXMAAAAAASAXAMAMAMXSAMMAMAAAX
SSMSAMASMMXSMSMSAAMSXSXAMXXMMXSASASASXSASMSSMXMXMAAXAMASMMMSMMMAXAMSMMSMMMXAAAMAMSASXSXMMAMAAMAXMASXSAMXMAMMSXMMSMMMMXMAXASMSMSSMMMAXMAMMMXM
XXAMASMMAXMMAAAMMSMAAMMSSSXSXAXASXSXSMSAMXMXMAMAMXAMXSAMAXXXMAXSSXXAAAAAAMSMMXSAXSAMXAXAMXSMMMMXMAXMXMXAMXSAMASAMXSMMXMASMMAAMAMAXSMMSSSSSSM
XMXMXMAXXMAMMMMMAAAMAMAAAXAMMMSMMMSMSAMXMMSMSASXSAMXXMAMXMXMASXAAMSSSSSSMMAMAMMMMMAMMASMSASMAMXMMAMXAMSASAMASXMASAMAMXMAXMXXMMAMSMSXAXAAXAAA
SMMSMAASMMMSXSMMXASMMAMSMMSMAAAAMXSASMMASXAAMMXAMXMMMSSMMAASAXMMMMXAAAMAMSMMMSAMMSMMXAAXXAXXAMASXSXSMMAXMMSMMXSMMXXAMXMMSSXMXMXMXAMMSMMMMSMM
SAAAAMMSAAASMXXASMMXXAXAMXASMSSSMAMXMASAXMXSSSSMSASAMAMAXSXSAMMSAMMMMMMMMAAAAXAMAAXXMMSSMAMSSSMSAMMAMAMXSXMMXAAMAXXSSMSAAAAXAMXMMAMAMAAMMXAX
SMMSXAMSMMMSASMMSAASXXXAAXAXMAXAMMSMSMMXXSAAXXAASASMMASMMMXMXMASASXAXAAAMXSMSMSMSSSMSAAAXXMSAAAMXMAMSAMMMASXMMSMSSMMAMMMSMASASAAMAMASMMSAMXM
XAAMMXMMAXAXMAAASMMMASMAMSMXASXMMAAAAXXMAMMXMMMMMAMXSXXXASXXAMAMAMMMSSSXSAMAXAAMAAMAMMXSMSSXSMMSAMMMXASXMAMXXMAMAAAXAMAXAMASASXSMAXXXAAMMSAM
SMSXSAASMMSMMSMMXAXMAMAMXAMMMMAXMSSSMMSAAXSASAAXMXMASMMSMMMXXMSSXSAXXAAAMAMAMSMMMSMSMSXXAMXAXXXSASMSXMAMMAMMMMMSSSMSSSXSMMMSASAMXSMSXSMSASAS
XAAAXSXMMAXAAXXMXSMMXSXMSAXAASXMMXAAAAAXXMSASAXSXMAMMXAAAASMAXAAASMMXMMMMMMXMAXXXAAAAXAMSMMAMXMSAMAAMSASXSMSAAXAAAAAXXXMXMMMMMASAMAMAAAMAXAM
MMMSMMMMMAMMXMASAAASAMAMXMSSMMSMMMMMMMSSSMMMMXMSAAXXSMSMMMXAXAMMMMASMXAXASMSMMSSSMSMSMMMAXSAMMAMXMXMMMAMAAASXXMMXMMMSMMSMMXAXSAMXMAMSMMMSMAM
XXAMASAMMMSMXSAMASXSASAMAMXMAMXMXMASXAXAAMXASAMMAMMMXAAXSSMSSMXAASAMAXMSXSAASAAAAXAXMASMXMSASAXAASASMMXMMMMMMSMSXMAXAAMAAMSSMMASXMXMXASAXSXM
XMASXMSXAAAXXMMXMXMSAMXSASMSXMXSAMXMASMSMMSASASXSMMAMMMSAASAAMMMMMMSMSAMXMXMMMSSMMMXSMMXMXXAMXXSXMAMMASMSSMMAAAXASMXSMMSSMAMXSSMMSSXMAMXMAMX
ASAMMMAMMXSXMMSAMAMMSMAMXSAMAMASAXAXAXAMXMXXMAMXAAXMMMMMXMMSSMMSAMXAAMMXSMXXXAAAAAXMSAMMSAMSMSXMXMAMMASMAMAMSSSMMMSXXAAAXMASXMAXMASXMSAMXXAS
MMMXAAMMSAXAAASMXXSAMMMSMXASAMASAMSMSSSMAMSSMAMSSMMSMAAAMXMAXAASASMMSMMXMASXMMSSMMMAXASAMXXAAXMAASAMMMXMAMXMAAAASASMSMMSXXMXAMMXMASXMAAXMASA
MAAMXMXAMASXMMSXSXMMSXSAMXAMMMAMAMMAAAASXSAAXAMXAAAAMSMXSAMSSMMSXMXXMAXAMAMAAMAMAASMSMMXSMSMSMMSMSASASMSXSAMXMMMMASASMAMMSSSMMMAMXXAMMMMMMXM
MSSSMASAMXMAXXXAAXAASMSASMSMXMASMMMMMSMMMMXSMSSSMMXSMXAXSAMXAXAXMAXAMMSSSSSSMMASMMMAAXAAXMAMXXMMXSASASAAMSXSXSMXMMMXXMAXXXAASMSSSXSAMASMSAMX
XAAAXASAMMSMMXMAMMMXSASAMAMASXMSMXXXXMASXAAXAXXAAAAXMMSMSMMSMMSSSSMSXAXXAMMAAMASAMXMSMMSXSASXSXXAMXMAMMMXSAMAXMASASXMMMSMMMMMXAXAAXAMXXAAXXM
MMSMMAXAMXAAXXMAMMMMMMMMMXMAXAMMMMSAMXMSAMXMAMSSMMMSAAMASAAAAAXMAAAMMMMMSMSMMMMSAMMMXAXMASMSAMMMMMMMXMXMXMAMXMSXSAXXAAAAMMMAXMMMMMMSSSMSMSSS
XAAXAMSMMSSSMMMASAAAAXAXAXMSSSMAAXAMXSXSXSXMAMMAMMMSMMSAMMSSMMXMMMMMAXXAXMSAMXASAMXAXAMXXMAMXMAAXAAMMSSMMSSMAMMMMMMSSMSXMASXSASMSAXMAXAMAAAA
MSSSSMAAXAAAMASAMXXXMSMMSAMXAAXMMSMMMSAMASXSAASAMAMMMAMASAAAASXMSMXSSXMXSASMMMMSSXMASXMSSSMSASMSSSSSXMAAMAASASAXXSAAAMXAMXSMSAMASMXMMMXMMMSM
MAAMMSMSMMMMMXMMSSMSAAAXMMAMMMSSXAAMASAMAMMMSXXXSASMMASXMMSSSMSAAXAMMAMAMMMSXAXMMXAAAXAAAAASXXMXAMXMASXMMXXSSSMSXMMSSMSSMAMASAMXMAMMXSXMXAAA
MSXSAMXAMSASMMMMAMAAXMAMXMAMXAAMXSMMASAMXSAMMXSXSASAMXMAMAAMAAMSMMXMMAMMSMAASXXXSSSXMMMMXMMMMSMMASXSAMASXXXXXXMSMSAXXAAXMAMXSAMXXMASAMMMSSSS
XXAMXXSAXSASAAAMASXMAXSMMXAMMMSSMXAMASAMXMXAAASMMAMXMASAMMXSMMMXXAXMXMSMAMSMXSXAMXAAAMAXSAMXAAAMAMAMXSXMSMMMMMMXAMMSMMMXXAXAMAMMXSXMASAXMAAX
XMSMXXMMMMMMMSXSMSAXSXMASXSSSXAXXMAMXSXMXXAMMMXAMXMSSXSMXSAAAAAAMSMSAMAXXXXMAAMMMASMXXASMXMASXSMMMAMMMMMAMAAAAAMSMAAXAAXMXMSMSMSAXASASXSMMMM
MMAMXMAAXAAXXXAAAXXMMAMAMXAAXMMSSMMSAMASMSMXAXMXMAMASMXMAMMXMMXMSAAXASASMMAMXMXAAXMXXMXMMASAMAAAXSAMXAASASMSSSMMXMSSSMSSXSAMAAAMASMMMXASMAMA
XMAXASXMSSXSAMMMSMAAMXMAMMMMMSAAAAAMAMMXAAASMSAASXMASXMMASMSXSAMXASXXMASASAMXSSMSSMMXMSASXSAMMMMMAAMSMMSASAXMAXMAMMMMMAAASAMAMXMAMMAMMMMAAXS
XSSSXXSAAAXMAMXAAXSMAASASAXAAMMSSMMSAMXMMMXMAMXXMAMASASAMXAAASXMSAMXMMXMAMASAMXXAAASAXSAMASXMXMSXMAMAAMMAMMMMAASASAAAMMSMMAMXXXXXASAMXMASMSA
MAASMSAMXSXASAMSSMXMSMSASXSMSSXMAXXSMSXXSMAMXMMMAAMMSMMMAMMMMMSMMASXMASXSSSMASAXSSMMXXMMMMMXMASAXXXSSSMMMMXMMSMSASXSXSAMMSXMAXSAMXSXSAXMASXX"""


def find(text):
    lines = text.split('\n')
    count = 0
    y = len(lines)
    x = len(lines[0])

    for i in range(y):
        for j in range(x):
            if lines[i][j] == 'X':
                if i<y-3 and lines[i+1][j]=='M' and lines[i+2][j]=='A' and lines[i+3][j]=='S':
                    count+=1
                if j<x-3 and lines[i][j+1]=='M' and lines[i][j+2]=='A' and lines[i][j+3]=='S':
                    count+=1
                if i>=3 and lines[i-1][j]=='M' and lines[i-2][j]=='A' and lines[i-3][j]=='S':
                    count+=1
                if j>=3 and lines[i][j-1]=='M' and lines[i][j-2]=='A' and lines[i][j-3]=='S':
                    count+=1
                if i>=3 and j>=3 and lines[i-1][j-1]=='M' and lines[i-2][j-2]=='A' and lines[i-3][j-3]=='S':
                    count += 1
                if i>=3 and j<x-3 and lines[i-1][j+1]=='M' and lines[i-2][j+2]=='A' and lines[i-3][j+3]=='S':
                    count += 1
                if i<y-3 and j>=3 and lines[i+1][j-1]=='M' and lines[i+2][j-2]=='A' and lines[i+3][j-3]=='S':
                    count += 1
                if i<y-3 and j<x-3 and lines[i+1][j+1]=='M' and lines[i+2][j+2]=='A' and lines[i+3][j+3]=='S':
                    count += 1

    print(count)


find(data)

def findmas(text):
    lines = text.split('\n')
    count = 0
    y = len(lines)
    x = len(lines[0])
    letters = defaultdict(lambda: 0)
    for i in range(y-2):
        for j in range(x-2):
            if lines[i+1][j+1] == 'A':
                letters['M'] = 0
                letters['S'] = 0
                letters[lines[i][j]] += 1
                letters[lines[i][j+2]] += 1
                letters[lines[i+2][j]] += 1
                letters[lines[i+2][j+2]] += 1
                if letters['M'] == 2 and letters['S'] == 2 and \
                    lines[i][j] != lines[i+2][j+2] and lines[i+2][j] != lines[i][j+2]:
                    count += 1
    print(count)

findmas(data)