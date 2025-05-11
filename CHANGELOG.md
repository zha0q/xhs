# Changelog

## dev

- Improve documentation
- Add more test function

## 0.2.13

### Fixed

- fix login phone and logon qrcode error

## 0.2.12

### Fixed

- fix get_note_by_id_from_html broken
- fix 461 and 471 should throw error

## 0.2.11

### Fixed

- fix image and video post error

## 0.2.10

### Added

- add get_notes_summary api
- add get_notes_statistics api

### Fixed

- send_code v1 to v2

## 0.2.8

### Added

- add get notification api

### Fixed

- trace id error when it contains spectrum

## 0.2.7

### Added

- add phone login api

## 0.2.6

### Fixed

- fix no watermark image url error

## 0.2.5

### Added

- add create image note api
- add create video note api

## 0.2.4

### Added

- add create note api

### Fixed

- fix cookie key with white space error

## 0.2.3

### Added

- add get self info v2 api
- add get home feed categories api

### Fixed

- fix basic usage is not work

## 0.2.2

### Added

- add a custom sign func to constructor

## 0.2.1

### Fixed

- fixed get_note_by_id_from_html with video note parse error

## 0.2.0

### Fixed

- fixed save_files_from_note_id error
- fixed get_user_all_notes abnormal notes catch error

## 0.1.9

### Fixed

- fixed get videos key error

## 0.1.8

### Added

- add get img and video to help

### Changed

- change get_img_url to help

## 0.1.7

### Fixed

- client init without cookie will casue a exception

### Added

- add get note by id from html api
- add ip block error exception
- add x-s-common sign

## 0.1.5

### Fixed

- fix get_user_all_notes lose note time and last_update_time

## 0.1.4

### Added

- add get user like notes
- add get user collect notes

## 0.1.3

### Added

- add get note comments
- add get note sub comments
- add get note all comments

## 0.1.2

### Added

- add get user all notes

### Changed

- change properties setter getter

## 0.1.1

### Added

- add search sort and note_type args

### Fixed

- fix save file error when invalid title

## 0.1.0

### Added

- add comment note api
- add delete note comment api
- add comment user api
- add follow user api
- add unfollow user api
- add collect note api
- add uncollect note api
- add like note api
- add like comment api
- add dislike note api
- add dislike comment api
- add get qrcode api
- add check qrcode api
- add save files from note id api

## 0.0.4

### Added

- add x-s 、search_id signature
- add get note by id api
- add get self info api
- add get user info api
- add get home feed api
- add get note by keyword api
- add get user notes api

## 0.0.3

### Added

- add pypi, doc, test ci actions

## 0.0.2

### Added

- add Sphinx Doc

## 0.0.1

### Added

- Structuring project (base on [Structuring Your Project](https://docs.python-guide.org/writing/structure/))
